from django.contrib import admin
from .models import Company, Car


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
