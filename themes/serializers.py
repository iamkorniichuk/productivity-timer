from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from commons.serializers import CurrentUserDefault, DefaultSupportNestedSerializer

from users.serializers import UserSerializer

from .models import Theme


class ThemeSerializer(DefaultSupportNestedSerializer):
    class Meta:
        model = Theme
        fields = "__all__"
        read_only_fields = [
            "is_main",
            "children",
        ]

    is_main = serializers.BooleanField(required=False)
    children = RecursiveField(many=True, required=False)
    user = UserSerializer(default=CurrentUserDefault(), read_only=True)


class NestedThemeSerializer(ThemeSerializer):
    children = None
    # TODO: Add PK user's field
