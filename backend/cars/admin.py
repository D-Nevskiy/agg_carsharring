from django.contrib import admin
from .models import EngineType, CarType, Company, Car


@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "model",
        "company",
        "engine_type",
        "car_type",
        "is_available",
        "latitude",
        "longitude",
    ]
    list_filter = ["company", "engine_type", "car_type", "is_available"]
    search_fields = ["name", "model", "company__name"]
