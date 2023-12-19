from django.contrib import admin
from cars.models import Car
from cars.models import CoordinatesCar


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(CoordinatesCar)
class CoordinatesAdmin(admin.ModelAdmin):
    pass
