from django.urls import path

from .apps import ThemesConfig
from .views import *


app_name = ThemesConfig.name

urlpatterns = [
    path("", ThemeList.as_view(), name="list"),
    path("<int:pk>", ThemeDetail.as_view(), name="detail"),
]
