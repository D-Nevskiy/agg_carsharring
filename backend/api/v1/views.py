from djoser.views import UserViewSet as DjoserUserViewSet

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .serializers import (
    UserSerializer,
    CarSerializer,
    CompanySerializer
)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car, Company


class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class CarListView(APIView):
    """Возвращает список всех автомобилей в системе."""
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyListView(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
