from rest_framework import serializers

from .models import Theme


# TODO: Add depth without sensitive information exposure
class ThemeSerializer(serializers.ModelSerializer):
    is_main = serializers.BooleanField(required=False)

    class Meta:
        model = Theme
        fields = "__all__"
        read_only_fields = [
            "is_main",
            "user",
        ]
