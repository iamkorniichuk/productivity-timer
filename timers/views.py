from rest_framework import generics
from commons.views import UserRelatedObjectsMixin, PrefetchRelatedManagersMixin

from .serializers import TimerSerializer
from .models import Timer


class TimerList(
    UserRelatedObjectsMixin, PrefetchRelatedManagersMixin, generics.ListCreateAPIView
):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()


class TimerDetail(
    UserRelatedObjectsMixin,
    PrefetchRelatedManagersMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()
