from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from commons.serializers import SerializeAnnotationsMixin

from users.serializers import USER_FIELD

from .models import Theme


class ThemeSerializer(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"

    children = RecursiveField(
        to="ChildThemeSerializer",
        many=True,
        required=False,
        read_only=True,
    )
    user = USER_FIELD


class ChildThemeSerializer(ThemeSerializer):
    user = None


class NestedThemeSerializer(ThemeSerializer):
    children = None
    user = None