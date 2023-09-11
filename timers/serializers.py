from rest_framework import serializers

from commons.serializers import (
    RepresentativePrimaryKeyRelatedField,
    SerializeAnnotationsMixin,
)


from users.serializers import USER_FIELD
from tasks.serializers import NestedTaskSerializer

from .models import Timer


class TimerSerializer(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = "__all__"

    user = USER_FIELD
    task = RepresentativePrimaryKeyRelatedField(
        serializer_class=NestedTaskSerializer,
        required=False,
    )
