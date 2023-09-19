from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import (
    RepresentativePrimaryKeyRelatedField,
    SerializeUrlMixin,
)


from users.serializers import USER_FIELD
from tasks.serializers import NestedTaskSerializer

from .models import Timer


class TimerSerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = Timer
        fields = "__all__"

    user = USER_FIELD
    task = RepresentativePrimaryKeyRelatedField(serializer_class=NestedTaskSerializer)


class NestedTimerSerializer(TimerSerializer):
    user = None
