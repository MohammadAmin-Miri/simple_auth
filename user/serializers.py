from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers

from user.models import CustomUser
from user.tasks import send_verification_code

user_model = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = user_model(**validated_data)
        user.set_password(password)
        user.save()
        send_verification_code.apply_async((validated_data.get('phone'), validated_data.get('email')))
        return user
