from django.urls import path

from .apps import TimersConfig
from .views import *


app_name = TimersConfig.name

urlpatterns = [
    path("", TimerList.as_view(), name="list"),
    path("<int:pk>", TimerDetail.as_view(), name="detail"),
]
