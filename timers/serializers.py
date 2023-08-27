from rest_framework import serializers

from .models import Timer


class TimerSerializer(serializers.ModelSerializer):
    is_datetime_set = serializers.BooleanField(required=False)
    datetime = serializers.DateTimeField(required=False)
    is_ended = serializers.BooleanField(required=False)
    duration = serializers.DurationField(required=False)
    is_completed = serializers.BooleanField(required=False)

    class Meta:
        model = Timer
        fields = "__all__"
        read_only_fields = [
            "is_datetime_set",
            "datetime",
            "is_ended",
            "duration",
            "is_completed",
            "user",
        ]
