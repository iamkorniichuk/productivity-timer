from django.urls import path

from .apps import TasksConfig

app_name = TasksConfig.name

from .views import *

urlpatterns = [
    path("", TaskList.as_view(), name="list"),
    path("<int:pk>", TaskDetail.as_view(), name="detail"),
]
