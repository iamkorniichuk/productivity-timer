from django.utils import timezone
from rest_framework import generics

from .serializers import PauseSerializer
from .models import Pause


class PauseList(generics.ListCreateAPIView):
    serializer_class = PauseSerializer
    queryset = Pause.objects.all()


# TODO: Add description about update `end`
class PauseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PauseSerializer
    queryset = Pause.objects.all()

    def update(self, request, *args, **kwargs):
        if not request.data:
            request.data["end"] = timezone.now()
            print(request.data)
        return super().update(request, *args, **kwargs)
