from django.urls import path

from .apps import UsersConfig
from .views import CurrentUserDetail


app_name = UsersConfig.name

urlpatterns = [
    path("current/", CurrentUserDetail.as_view(), name="current_detail"),
]
