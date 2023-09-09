from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from users.serializers import USER_FIELD

from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"
        read_only_fields = [
            "is_main",
            "children",
            "user",
        ]

    is_main = serializers.BooleanField(required=False)
    children = RecursiveField(many=True, required=False)
    user = USER_FIELD


class NestedThemeSerializer(ThemeSerializer):
    children = None
    user = None
