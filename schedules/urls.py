from django.urls import path

from .apps import SchedulesConfig
from .views import *


app_name = SchedulesConfig.name

urlpatterns = [
    # TODO: Think about moving frequency to a separate app
    path("frequencies/", FrequencyList.as_view(), name="frequency_list"),
    path("frequencies/<int:pk>", FrequencyDetail.as_view(), name="frequency_detail"),
]
