from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import SerializeUrlMixin

from .models import Frequency


class FrequencySerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = Frequency
        fields = "__all__"
