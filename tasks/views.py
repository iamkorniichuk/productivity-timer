from rest_framework import generics
from commons.views import UserRelatedObjectsMixin

from .serializers import TaskSerializer
from .models import Task


class TaskList(UserRelatedObjectsMixin, generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetail(UserRelatedObjectsMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
