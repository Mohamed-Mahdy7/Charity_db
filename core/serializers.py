from djoser.serializers import UserCreateSerializer as BaseUser,\
        UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer\
    as SimpleJwtToken
from rest_framework import serializers
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class UserCreateSerializer(BaseUser):
    class Meta(BaseUser.Meta):
        fields = [
            "id", "email", "first_name",
            "last_name", "user_name", "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=["id", "email"]


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

class CustomTokenObtainPairSerializer(SimpleJwtToken):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update ({
            "id": self.user.id,
            "email": self.user.email,
            "user_name": self.user.user_name,
            "role": "admin" if self.user.is_superuser else "user",
        })
        return data