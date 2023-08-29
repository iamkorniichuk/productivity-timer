from django.urls import path

from .apps import ThemesConfig

app_name = ThemesConfig.name

from .views import *

urlpatterns = [
    path("", ThemeList.as_view(), name="list"),
    path("<int:pk>", ThemeDetail.as_view(), name="detail"),
]
