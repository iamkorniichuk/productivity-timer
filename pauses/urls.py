from django.urls import path
from .apps import PausesConfig

app_name = PausesConfig.name


from .views import *

urlpatterns = [
    path("", PauseList.as_view(), name="list"),
    path("<int:pk>", PauseDetail.as_view(), name="detail"),
]
