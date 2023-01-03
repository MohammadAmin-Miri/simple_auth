from rest_framework import generics
from rest_framework.permissions import AllowAny

from .exceptions import PhoneOrEmailNotEntered
from .serializers import CustomUserSerializer


class SignupUser(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        if 'phone' not in data and 'email' not in data:
            raise PhoneOrEmailNotEntered
        serializer.save()
