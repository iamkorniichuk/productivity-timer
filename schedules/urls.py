from django.urls import path

from .apps import SchedulesConfig
from .views import *


app_name = SchedulesConfig.name

urlpatterns = [
    path("frequencies/", FrequencyList.as_view(), name="frequency_list"),
    path("frequencies/<int:pk>", FrequencyDetail.as_view(), name="frequency_detail"),
]
