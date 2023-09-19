from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import (
    RepresentativePrimaryKeyRelatedField,
    SerializeUrlMixin,
)


from timers.serializers import NestedTimerSerializer

from .models import Pause


class PauseSerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = Pause
        fields = "__all__"

    timer = RepresentativePrimaryKeyRelatedField(serializer_class=NestedTimerSerializer)
