from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email and phone are the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone=None, email=None, password=None, **extra_fields):
        """
        Create and save a User with the given phone, email and password.
        """
        if phone and email:
            email = self.normalize_email(email)
            user = self.model(email=email, phone=phone, **extra_fields)
        elif email:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
        elif phone:
            user = self.model(phone=phone, **extra_fields)
        else:
            raise ValueError(_('An email address or a phone number must be entered'))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone=None, email=None, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, email, password, **extra_fields)
