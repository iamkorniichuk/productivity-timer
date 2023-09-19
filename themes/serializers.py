from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import SerializeUrlMixin

from users.serializers import USER_FIELD

from .models import Theme


class ThemeSerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
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
