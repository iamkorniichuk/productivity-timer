from django.urls import path

from .apps import TimersConfig

app_name = TimersConfig.name

from .views import *

urlpatterns = [
    path("", TimerList.as_view(), name="list"),
    path("<int:pk>", TimerDetail.as_view(), name="detail"),
]
