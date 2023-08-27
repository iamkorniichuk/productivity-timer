from rest_framework import generics

from .serializers import TaskSerializer
from .models import Task


# TODO: Return after create serialized data
class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
