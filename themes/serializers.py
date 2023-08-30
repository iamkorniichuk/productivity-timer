from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"
        read_only_fields = [
            "is_main",
            "user",
            "children",
        ]

    is_main = serializers.BooleanField(required=False)
    children = RecursiveField(many=True, required=False)
