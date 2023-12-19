from .models import Car
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CarSerializer
from .filters import CarFilter
from django_filters.rest_framework import DjangoFilterBackend


class CarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = CarFilter
