from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from commons.serializers import RepresentativePrimaryKeyRelatedField
from commons.utils import model_to_data

from users.serializers import USER_FIELD
from schedules.serializers import FrequencySerializer
from themes.serializers import NestedThemeSerializer

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "is_current_version",
            "is_draft",
            "is_disposable",
            "completed_timers",
            "remaining_timers",
            "previous_version",
        ]

    is_current_version = serializers.BooleanField(required=False)
    is_draft = serializers.BooleanField(required=False)
    is_disposable = serializers.BooleanField(required=False)
    completed_timers = serializers.IntegerField(required=False)
    remaining_timers = serializers.IntegerField(required=False)
    user = USER_FIELD
    frequency = RepresentativePrimaryKeyRelatedField(
        serializer_class=FrequencySerializer,
        required=False,
    )
    theme = RepresentativePrimaryKeyRelatedField(
        serializer_class=NestedThemeSerializer,
        required=False,
    )
    previous_version = RecursiveField("PreviousVersionTaskSerializer", required=False)

    def update(self, instance, validated_data):
        if instance.completed_timers > 0:  # TODO: Change to OVERALL completed timers
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
