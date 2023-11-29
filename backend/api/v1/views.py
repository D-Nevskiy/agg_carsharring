from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .serializers import RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = User(
                phone_number=request.data.get("phone_number"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                email=request.data.get("email"),
            )

            user.save()

            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer