from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import (
    RepresentativePrimaryKeyRelatedField,
    SerializeUrlMixin,
)
from commons.utils import model_to_data

from users.serializers import USER_FIELD
from schedules.serializers import FrequencySerializer
from themes.serializers import NestedThemeSerializer

from .models import Task


class TaskSerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = Task
        fields = "__all__"

    user = USER_FIELD
    frequency = RepresentativePrimaryKeyRelatedField(
        serializer_class=FrequencySerializer,
        required=False,
    )
    theme = RepresentativePrimaryKeyRelatedField(
        serializer_class=NestedThemeSerializer,
        required=False,
    )
    previous_version = RecursiveField(
        "PreviousVersionTaskSerializer",
        required=False,
        read_only=True,
    )

    def update(self, instance, validated_data):
        if instance.all_completed_timers > 0:
            data = model_to_data(instance, exclude=["id"])
            data["previous_version"] = instance
            data.update(validated_data)
            return super().create(data)
        return super().update(instance, validated_data)


class PreviousVersionTaskSerializer(TaskSerializer):
    user = None


class NestedTaskSerializer(TaskSerializer):
    user = None
    frequency = None
    theme = None
