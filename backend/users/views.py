from djoser.views import UserViewSet as DjoserUserViewSet

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
