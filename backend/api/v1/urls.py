from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework import routers

from .views import PublicUserViewSet
from cars.views import CarViewSet

app_name = "api"


router_v1 = routers.DefaultRouter()

router_v1.register("users", PublicUserViewSet, "users")
router_v1.register("cars", CarViewSet, "users")


urlpatterns = [
    path("", include(router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
]
