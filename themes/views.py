from rest_framework import generics

from .serializers import ThemeSerializer
from .models import Theme


class ThemeList(generics.ListCreateAPIView):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        return Theme.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        return Theme.objects.filter(user=self.request.user)
