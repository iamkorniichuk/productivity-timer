from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from .validators import PasswordValidator

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with the provided credentials"
        )


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [PasswordValidator()],
            },
        }

    def create(self, validated_data):
        User = self.Meta.model
        return User.objects.create_user(**validated_data)
