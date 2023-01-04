import random

from rest_framework_simplejwt.tokens import RefreshToken


def code_generator():
    return str(random.randint(pow(10, 4), (pow(10, 5) - 1)))


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }
