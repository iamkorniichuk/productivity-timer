from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from commons.serializers import CurrentUserDefault, DefaultSupportNestedMixin

from users.serializers import UserSerializer

from .models import Theme


class ThemeSerializer(DefaultSupportNestedMixin, WritableNestedModelSerializer):
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
    user = UserSerializer(required=False, default=CurrentUserDefault())


class NestedThemeSerializer(ThemeSerializer):
    children = None
    # TODO: Add PK user's field
