from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    is_draft = serializers.BooleanField(required=False)
    is_disposable = serializers.BooleanField(required=False)
    completed_timers = serializers.IntegerField(required=False)
    remaining_timers = serializers.IntegerField(required=False)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "is_draft",
            "is_disposable",
            "completed_timers",
            "remaining_timers",
            "user",
        ]
