from django.urls import include, path
from .spectacular.urls import urlpatterns as doc_urls

from .views import RegistrationAPIView, UsersAPIView


app_name = "api"


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path("users/", UsersAPIView.as_view(), name="list_users"),
    path("", include("drfpasswordless.urls")),
]

urlpatterns += doc_urls
