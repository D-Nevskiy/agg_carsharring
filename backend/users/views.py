from djoser.views import UserViewSet as DjoserUserViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


@extend_schema(tags=["Пользователи"])
@extend_schema_view(
    list=extend_schema(summary='Список пользователей'),
    retrieve=extend_schema(summary='Получение профиля одного пользователя'),
    create=extend_schema(summary='Создание пользователя'),
    update=extend_schema(summary='Полное обновление пользователя'),
    partial_update=extend_schema(summary='Частичное обновление пользователя'),
    destroy=extend_schema(summary='Удаление пользователя'),
)
class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
