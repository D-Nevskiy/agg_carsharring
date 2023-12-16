from .models import Car, CoordinatesCar
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CoodinatesCarSerializer(ModelSerializer):
    class Meta:
        model = CoordinatesCar
        fields = ('latitude', 'longitude')


class CarSerializer(ModelSerializer):
    coordinates = CoodinatesCarSerializer()

    class Meta:
        model = Car
        fields = '__all__'
