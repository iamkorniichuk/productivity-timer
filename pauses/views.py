from rest_framework import generics

from .serializers import PauseSerializer
from .models import Pause


class PauseList(generics.ListCreateAPIView):
    serializer_class = PauseSerializer
    queryset = Pause.objects.all()


class PauseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PauseSerializer
    queryset = Pause.objects.all()
