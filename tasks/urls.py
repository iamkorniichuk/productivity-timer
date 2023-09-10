from django.urls import path

from .apps import TasksConfig
from .views import *


app_name = TasksConfig.name

urlpatterns = [
    path("", TaskList.as_view(), name="list"),
    path("<int:pk>", TaskDetail.as_view(), name="detail"),
]
