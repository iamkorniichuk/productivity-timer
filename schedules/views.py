from rest_framework import generics

from .serializers import FrequencySerializer
from .models import Frequency


class FrequencyList(generics.ListCreateAPIView):
    serializer_class = FrequencySerializer
    queryset = Frequency.objects.all()


class FrequencyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FrequencySerializer
    queryset = Frequency.objects.all()
