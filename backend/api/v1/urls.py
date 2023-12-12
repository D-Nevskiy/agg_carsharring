from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework import routers

from .views import (
    PublicUserViewSet,
    CarListView,
    CompanyListView,
)

app_name = "api"

router_v1 = routers.DefaultRouter()

router_v1.register("users", PublicUserViewSet, "users")

urlpatterns = [
    path("", include(router_v1.urls)),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("companies/", CompanyListView.as_view(), name="companies"),
    path("auth/", include("djoser.urls.authtoken")),
    path("schema/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]
