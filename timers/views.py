from django.utils import timezone
from rest_framework import generics

from commons.views import UserRelatedObjectsMixin

from .serializers import TimerSerializer
from .models import Timer


class TimerList(UserRelatedObjectsMixin, generics.ListCreateAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()


# TODO: Add description about update `end`
class TimerDetail(UserRelatedObjectsMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()

    def update(self, request, *args, **kwargs):
        if not request.data:
            request.data["end"] = timezone.now()
            print(request.data)
        return super().update(request, *args, **kwargs)
