from rest_framework import serializers

from .models import Frequency


class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = "__all__"
        read_only_fields = [
            "start",
            "end",
            "remaining_time",
            "duration",
        ]

    start = serializers.DateTimeField(required=False)
    end = serializers.DateTimeField(required=False)
    remaining_time = serializers.DurationField(required=False)
    duration = serializers.DurationField(required=False)
