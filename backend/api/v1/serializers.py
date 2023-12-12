from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from users.models import User
from cars.models import Car, Company


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


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]


class CarSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Car
        fields = [
            "id",
            "is_available",
            "company",
            "name",
            "model",
            "engine_type",
            "car_type",
            "rating",
            "coefficient",
            "child_seat",
            "latitude",
            "longitude",
        ]