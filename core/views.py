from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView as BaseToken
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        
        user_data = {
            "id": user.id,
            "email": user.email,
            "username": user.user_name,
            "role": "admin" if user.is_superuser else "user",
        }
        response = Response(user_data, status=status.HTTP_201_CREATED)
        
        response.set_cookie(
            key='access_token', 
            value=access,
            httponly=True,
            secure=False,
            samesite='lax'
        )
        response.set_cookie(
            key='refresh_token',
            value=refresh,
            httponly=True,
            secure=False,
            samesite='lax'
        )
        return response

class LoginView(BaseToken):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        base_response = super().post(request, *args, **kwargs)
        if base_response.status_code != 200:
            return base_response
        
        data = base_response.data
        refresh = data.get("refresh")
        access = data.get("access")
        
        user_data = {k: v for k, v in data.items()
                        if k not in ["refresh", "access"]}
        response = Response(user_data)
        if access:
            response.set_cookie(
                key='access_token', 
                value=access,
                httponly=True,
                secure=False,
                samesite='lax'
            )
        if refresh:
            response.set_cookie(
                key='refresh_token',
                value=refresh,
                httponly=True,
                secure=False,
                samesite='lax'
            )
        return response

class RefreshTokenView(APIView):
    def post(self, request):
        print("REFRESHING THE TOKEN")
        refresh_token = request.COOKIES.get("refresh_token")
        
        if not refresh_token:
            return Response({"error": "No refresh token"},
                            status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            # print("refresh:",refresh, "refresh_token:",refresh_token)
            new_access = str(refresh.access_token)
            response = Response({"access": new_access})
            response.set_cookie(
                key="access_token",
                value=new_access,
                httponly=True,
                secure=False,  
                samesite="lax"
                )
            return response
        except Exception:
            return Response({"error": "Invalid refresh token"},
                            status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out"})
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
