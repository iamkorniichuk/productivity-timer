from rest_framework import serializers

from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"
        read_only_fields = [
            "is_main",
            "user",
        ]

    is_main = serializers.BooleanField(required=False)
