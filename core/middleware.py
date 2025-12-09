from django.utils.deprecation import MiddlewareMixin

class AutoRefreshJWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print("MIDDLEWARE: process_request — request.COOKIES:", request.COOKIES)
        # print("MIDDLEWARE: process_request — HTTP_COOKIE header:", request.META.get("HTTP_COOKIE"))
        # print("MIDDLEWARE: process_request — Origin:", request.META.get("HTTP_ORIGIN"))
        return None
    
    def process_response(self, request, response):
        # print("THIS IS MIDDLEWARE")
        if hasattr(request, "_new_access_token"):
            print("MIDDLEWARE: setting new access token cookie")
            response.set_cookie(
                key="access_token",
                value=request._new_access_token,
                httponly=True,
                secure=False,   # set True in production (HTTPS)
                samesite="Lax"
            )
        return response