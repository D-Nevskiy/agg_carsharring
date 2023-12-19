import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
    type_car = django_filters.rest_framework.BaseInFilter()
    company = django_filters.rest_framework.BaseInFilter()
    type_engine = django_filters.rest_framework.BaseInFilter()
    power_reserve = django_filters.rest_framework.BaseInFilter()

    class Meta:
        model = Car
        fields = [
            'company',
            'type_car',
            'rating',
            'power_reserve',
            'child_seat',
            'type_engine',
            'model',
            'is_available',
        ]
