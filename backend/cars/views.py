from django.db.transaction import atomic

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer


class CarViewSet(ModelViewSet):
    """Представление для работы с публичными данными автомобилей."""

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    @atomic
    def create(self, request, *args, **kwargs):
        """Создать новый автомобиль."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
