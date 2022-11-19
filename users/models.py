from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from users.validators import username_validator


class CustomUserManager(BaseUserManager):
    error_message = {
        "password_mismatch": "The password doesn't match.",
        "password_too_short": "Password is too short. Minimum 8 characters."
    }
    MINIMUM_PASSWORD_LENGTH = 8

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, password2, **other_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, password=password, **other_fields)

        user = self.validate_password(user, password2)

        user.set_password(password)
        user.save()
        return user

    def validate_password(self, user_instance, password2):
        password = user_instance.password

        if len(password) < self.MINIMUM_PASSWORD_LENGTH:
            raise ValidationError(message=self.error_message["password_too_short"], code="password_too_short")

        if password != password2:
            raise ValidationError(message=self.error_message["password_mismatch"], code="password_mismatch")

        return user_instance


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, validators=[username_validator])
    email = models.EmailField('Email', unique=True)
    joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
