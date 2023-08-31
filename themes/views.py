from rest_framework import generics
from commons.views import UserRelatedObjectsMixin

from .serializers import ThemeSerializer
from .models import Theme


class ThemeList(UserRelatedObjectsMixin, generics.ListCreateAPIView):
    serializer_class = ThemeSerializer
    queryset = Theme.main_objects.all()


class ThemeDetail(UserRelatedObjectsMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ThemeSerializer
    queryset = Theme.main_objects.all()
