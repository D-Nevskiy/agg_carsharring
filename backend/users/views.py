from django.shortcuts import get_object_or_404

from djoser.views import UserViewSet as DjoserUserViewSet

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.utils import generate_reset_code, send_confirmation_code

from .models import User
from .serializers import (
    ResetCodeSerializer,
    SetUserPasswordSerializer,
    UserSerializer,
)


@extend_schema(tags=["Пользователи"])
@extend_schema_view(
    list=extend_schema(summary="Список пользователей"),
    retrieve=extend_schema(summary="Получение профиля одного пользователя"),
    create=extend_schema(summary="Создание пользователя"),
    update=extend_schema(summary="Полное обновление пользователя"),
    partial_update=extend_schema(summary="Частичное обновление пользователя"),
    destroy=extend_schema(summary="Удаление пользователя"),
    me=extend_schema(summary="Данные текущего пользователя"),
)
class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "reset_code":
            return ResetCodeSerializer
        if self.action == "set_user_password":
            return SetUserPasswordSerializer

        return UserSerializer

    @action(
        detail=False,
        url_path="reset-code",
        permission_classes=[AllowAny],
        methods=["post"],
    )
    def reset_code(self, request):
        serializer = ResetCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError(
                {"error": "Пользователь с указанной почтой не найден."}
            )

        code = generate_reset_code()

        user.password_reset_code = code
        user.save()

        send_confirmation_code(user.email, code)

        return Response(
            {"success": "Код успешно отправлен на почту"},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=False,
        url_path="set-user-password",
        permission_classes=[AllowAny],
        methods=["post"],
    )
    def set_user_password(self, request):
        serializer = SetUserPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        code = serializer.validated_data.get("code")
        password = serializer.validated_data.get("password")

        if not email or not code or not password:
            raise ValidationError(
                {"error": "Почта, код и новый пароль обязательны."}
            )

        user = get_object_or_404(User, email=email)

        if not user.password_reset_code or user.password_reset_code != code:
            raise ValidationError({"error": "Неверный код для сброса пароля."})

        user.set_password(password)
        user.password_reset_code = None
        user.save()

        return Response(
            {"success": "Пароль успешно изменен."},
            status=status.HTTP_200_OK,
        )
