from django.urls import path

from .apps import SchedulesConfig

app_name = SchedulesConfig.name

from .views import *

urlpatterns = [
    # TODO: Think about moving frequency to a separate app
    path("frequencies/", FrequencyList.as_view(), name="frequency_list"),
    path("frequencies/<int:pk>", FrequencyDetail.as_view(), name="frequency_detail"),
]
