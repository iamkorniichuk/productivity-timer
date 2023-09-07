from rest_framework import serializers
from commons.serializers import CurrentUserDefault, DefaultSupportNestedSerializer

from users.serializers import UserSerializer
from schedules.serializers import FrequencySerializer
from themes.serializers import NestedThemeSerializer

from .models import Task


class TaskSerializer(DefaultSupportNestedSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "is_draft",
            "is_disposable",
            "completed_timers",
            "remaining_timers",
        ]

    is_draft = serializers.BooleanField(required=False)
    is_disposable = serializers.BooleanField(required=False)
    completed_timers = serializers.IntegerField(required=False)
    remaining_timers = serializers.IntegerField(required=False)
    user = UserSerializer(default=CurrentUserDefault(), read_only=True)
    frequency = FrequencySerializer(required=False)
    theme = NestedThemeSerializer(required=False)


class NestedTaskSerializer(TaskSerializer):
    pass
