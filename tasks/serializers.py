from rest_framework import serializers

from users.serializers import UserSerializer
from schedules.serializers import FrequencySerializer
from themes.serializers import NestedThemeSerializer

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "is_draft",
            "is_disposable",
            "completed_timers",
            "remaining_timers",
            "user",
            "frequency",
            "theme",
        ]

    is_draft = serializers.BooleanField(required=False)
    is_disposable = serializers.BooleanField(required=False)
    completed_timers = serializers.IntegerField(required=False)
    remaining_timers = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)
    frequency = FrequencySerializer(required=False)
    theme = NestedThemeSerializer(required=False)


class NestedTaskSerializer(TaskSerializer):
    user = None
