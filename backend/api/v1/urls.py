from django.urls import path

from .views import RegistrationAPIView, UsersAPIView


app_name = "api"


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path('users/', UsersAPIView.as_view(), name='list_users')
]
