from django.urls import include, path
from .spectacular.urls import urlpatterns as doc_urls

from .views import (
    CarListView,
    RegistrationAPIView,
    UsersAPIView,
    EngineTypeListView,
    CarTypeListView,
    CompanyListView,
)


app_name = "api"


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path("users/", UsersAPIView.as_view(), name="list_users"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("engine/", EngineTypeListView.as_view(), name="car-list"),
    path("cars-type/", CarTypeListView.as_view(), name="cars-type"),
    path("companies/", CompanyListView.as_view(), name="companies"),
    path("", include("drfpasswordless.urls")),
]

urlpatterns += doc_urls
