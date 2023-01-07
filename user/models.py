from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

regex_validator = RegexValidator(regex="^[+]?[0-9]{10,12}$", message="Please enter a valid phone number")


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=12, unique=True, validators=[regex_validator], null=True)
    email = models.EmailField(_('email address'), unique=True, null=True)
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.phone:
            return self.phone
        elif self.email:
            return self.email
        else:
            return str(self.id)
