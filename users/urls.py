from django.urls import path

from .apps import UsersConfig
from .views import LoginView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
