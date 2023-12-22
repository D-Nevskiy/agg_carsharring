from rest_framework import serializers

from .models import Car, CoordinatesCar


class CoordinatesCarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели CoordinatesCar."""

    class Meta:
        model = CoordinatesCar
        fields = ("latitude", "longitude")


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Car."""

    coordinates = CoordinatesCarSerializer()

    class Meta:
        model = Car
        fields = "__all__"

    def validate_state_number(self, value):
        """
        Проверка уникальности номера состояния.
        """
        if Car.objects.filter(state_number=value).exists():
            raise serializers.ValidationError(
                "Автомобиль с таким номером уже существует."
            )
        return value

    def create(self, validated_data):
        coordinates_data = validated_data.pop("coordinates")
        coordinates_serializer = CoordinatesCarSerializer(
            data=coordinates_data,
        )

        if coordinates_serializer.is_valid():
            coordinates_instance = coordinates_serializer.save()
            validated_data["coordinates"] = coordinates_instance

            # Проверяем уникальность номера состояния
            self.validate_state_number(validated_data.get("state_number"))

            car = Car.objects.create(**validated_data)
            return car

        raise serializers.ValidationError("Ошибка валидации координат")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["rating"] = float(data["rating"])
        return data
