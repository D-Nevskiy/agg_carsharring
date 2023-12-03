from rest_framework import serializers

from cars.models import Car, EngineType, CarType, Company
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


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = ["id", "name"]


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ["id", "name"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]


class CarSerializer(serializers.ModelSerializer):
    engine_type = EngineTypeSerializer()
    car_type = CarTypeSerializer()
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
