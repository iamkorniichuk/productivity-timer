from django.urls import path

from .apps import UsersConfig
from .views import LoginView, SignUpView, LogoutView, LogoutAllView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logout-all/", LogoutAllView.as_view(), name="logout_all"),
]
