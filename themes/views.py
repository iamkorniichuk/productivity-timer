from rest_framework import generics
from commons.views import UserRelatedObjectsMixin, PrefetchRelatedManagersMixin

from .serializers import ThemeSerializer
from .models import Theme


# TODO: Fix: all methods interact with main_objects queryset
class ThemeList(
    UserRelatedObjectsMixin, PrefetchRelatedManagersMixin, generics.ListCreateAPIView
):
    serializer_class = ThemeSerializer
    queryset = Theme.main_objects.all()


class ThemeDetail(
    UserRelatedObjectsMixin,
    PrefetchRelatedManagersMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    serializer_class = ThemeSerializer
    queryset = Theme.main_objects.all()
