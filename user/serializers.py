from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers

from user.exceptions import VerificationCodeExpiredOrInvalid, VerificationCodeInvalid
from user.models import CustomUser
from user.tasks import send_verification_code
from user.utils import get_tokens_for_user

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


class VerifyUserPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, write_only=True)
    code = serializers.CharField(write_only=True)
    phone_verified = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        phone = validated_data.get('phone')
        valid_code = cache.get(phone)
        if not valid_code:
            raise VerificationCodeExpiredOrInvalid
        if validated_data.get('code') != valid_code:
            raise VerificationCodeInvalid
        user_model.objects.filter(phone=phone).update(phone_verified=True)
        return {'phone_verified': True}


class VerifyUserEmailSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    code = serializers.CharField(write_only=True)
    email_verified = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        valid_code = cache.get(email)
        if not valid_code:
            raise VerificationCodeExpiredOrInvalid
        if validated_data.get('code') != valid_code:
            raise VerificationCodeInvalid
        user_model.objects.filter(email=email).update(email_verified=True)
        return {'email_verified': True}
