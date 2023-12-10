from djoser.serializers import UserCreateSerializer
from users.models import User


class UserSerializer(UserCreateSerializer):
    """
    Сериализатор для модели пользователя .
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
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
