from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from users.models import User

from .serializers import CarSerializer, RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):
    """Регистрирует пользователя по номеру телефона, обновляет данные пользователя,
    если уже существует, и возвращает сообщение о успешной регистрации."""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        mobile = request.data.get("mobile")
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Проверяем существование пользователя по номеру телефона
            user = get_object_or_404(get_user_model(), mobile=mobile)

            # Если пользователь существует, обновляем его данные
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.email = request.data["email"]
            user.save()

            return Response(
                {
                    "message": "Регистрация прошла успешно, ожидайте подтверждения."
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UsersAPIView(ListAPIView):
    """Возвращает список всех пользователей в системе."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarListView(APIView):
    """Возвращает список всех автомобилей в системе."""

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
