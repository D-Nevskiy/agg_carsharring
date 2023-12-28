from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework import routers

from cars.views import CarViewSet, CarInMapViewSet
from users.views import PublicUserViewSet

from .router_settings import CustomDjoserUserRouter

app_name = "api"

# Routers v1
router_v1 = routers.DefaultRouter()
user_router_v1 = CustomDjoserUserRouter()

# Register
user_router_v1.register("users", PublicUserViewSet, "users")
router_v1.register("cars", CarViewSet, "cars")
router_v1.register("cars_map", CarInMapViewSet, "car_in_map")


# URL
urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include(user_router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
]
