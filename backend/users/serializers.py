from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

from .models import User


class UserSerializer(UserCreateSerializer):
    """
    Сериализатор для модели пользователя .
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def to_representation(self, instance):
        """
        Преобразует объект пользователя в представление JSON.
        """
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request.method == "GET":
            data.pop("password", None)

        return data


class ResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class SetUserPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "email",
            "code",
            "password",
        ]
