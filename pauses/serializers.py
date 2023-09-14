from rest_framework import serializers

from commons.serializers import (
    RepresentativePrimaryKeyRelatedField,
    SerializeAnnotationsMixin,
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
