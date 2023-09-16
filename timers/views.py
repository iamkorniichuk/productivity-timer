from rest_framework import generics

from commons.views import UserRelatedObjectsMixin

from .serializers import TimerSerializer
from .models import Timer


class TimerList(UserRelatedObjectsMixin, generics.ListCreateAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()


class TimerDetail(UserRelatedObjectsMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()
