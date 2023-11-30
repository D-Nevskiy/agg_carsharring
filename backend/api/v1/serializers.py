from rest_framework import serializers

from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
