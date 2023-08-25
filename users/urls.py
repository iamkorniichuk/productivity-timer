from django.urls import path

from .apps import UsersConfig
from .views import LoginView, SignUpView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
]
