from rest_framework import serializers

from commons.serializers import CurrentUserDefault
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "is_active",
            "last_login",
            "is_staff",
            "groups",
            "user_permissions",
        ]
        read_only_fields = [
            "email",
            "is_active",
            "last_login",
            "is_staff",
            "groups",
            "user_permissions",
        ]


USER_FIELD = UserSerializer(
    default=CurrentUserDefault(),
    read_only=True,
)
