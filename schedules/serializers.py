from rest_framework import serializers

from commons.serializers import SerializeAnnotationsMixin

from .models import Frequency


class FrequencySerializer(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = "__all__"
