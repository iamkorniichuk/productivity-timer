from rest_framework import generics
from commons.views import UserRelatedObjectsMixin, PrefetchRelatedManagersMixin

from .serializers import TaskSerializer
from .models import Task


class TaskList(
    UserRelatedObjectsMixin, PrefetchRelatedManagersMixin, generics.ListCreateAPIView
):
    serializer_class = TaskSerializer
    queryset = Task.current_version_objects.all()


class TaskDetail(
    UserRelatedObjectsMixin,
    PrefetchRelatedManagersMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
