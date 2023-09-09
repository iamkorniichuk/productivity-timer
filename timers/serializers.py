from rest_framework import serializers
from commons.serializers import CurrentUserDefault, RepresentativePrimaryKeyRelatedField


from users.serializers import UserSerializer
from tasks.serializers import NestedTaskSerializer

from .models import Timer


class TimerSerializer(serializers.ModelSerializer):
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

    is_datetime_set = serializers.BooleanField(required=False)
    datetime = serializers.DateTimeField(required=False)
    is_ended = serializers.BooleanField(required=False)
    duration = serializers.DurationField(required=False)
    is_completed = serializers.BooleanField(required=False)
    # TODO: Fix declaring read_only in meta doesn't work for this type
    user = RepresentativePrimaryKeyRelatedField(
        serializer_class=UserSerializer,
        default=CurrentUserDefault(),
        read_only=True,
    )
    task = RepresentativePrimaryKeyRelatedField(
        serializer_class=NestedTaskSerializer,
        required=False,
    )
