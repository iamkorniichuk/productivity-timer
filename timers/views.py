from rest_framework import generics

from .serializers import TimerSerializer
from .models import Timer


class TimerList(generics.ListCreateAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TimerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()
