from .models import Car
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CarSerializer


class CarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
