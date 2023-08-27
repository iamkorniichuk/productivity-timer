from django.urls import path

from .apps import UsersConfig

app_name = UsersConfig.name

from .views import CurrentUserDetail

urlpatterns = [
    path("current/", CurrentUserDetail.as_view(), name="current_detail"),
]
