from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from knox.settings import knox_settings
from knox.views import LogoutView as KnoxLogoutView, LogoutAllView as KnoxLogoutAllView

from .serializers import SignUpSerializer


# TODO: Rewrite when new django-rest-knox version releases (self.create_token only)
class LoginView(generics.GenericAPIView):
    serializer_class = knox_settings.USER_SERIALIZER
    permission_classes = [permissions.AllowAny]

    def get_serializer_data(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def post(self, request, *args, **kwargs):
        user = self.get_serializer_data(request)
        instance, token = AuthToken.objects.create(user)
        return Response(
            {
                "user": SignUpSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token,
            }
        )


class SignUpView(LoginView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_data(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.create(serializer.validated_data)


class LogoutView(KnoxLogoutView):
    def post(self, request, format=None):
        super().post(request, format)
        return Response({"message": "Successful logout"})


class LogoutAllView(KnoxLogoutAllView):
    def post(self, request, format=None):
        super().post(request, format)
        return Response({"message": "Successful logout from all devices"})
