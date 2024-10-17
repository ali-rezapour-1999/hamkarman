from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone_number field must be set")
        iran_phone_regex = RegexValidator(
            regex=r'^(9\d{9})$',  # Matches numbers starting with 9 and having 9 digits
            message=_("Phone number must be entered in the format: '9123456789'. Up to 10 digits allowed.")
        )
        iran_phone_regex(phone_number)  
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(BaseModel ,AbstractBaseUser, PermissionsMixin ):
    iran_phone_regex = RegexValidator(
        regex=r'^(9\d{9})$',  # Matches numbers starting with 9 and having 9 digits
        message=_("Phone number must be entered in the format: '9123456789'. Up to 10 digits allowed.")
    )
    phone_number = models.CharField(
        validators=[iran_phone_regex],
        max_length=10 ,
        unique=True
    )
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']


