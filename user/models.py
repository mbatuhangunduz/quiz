from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin, Group
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):  # ability to create user and superuser

    def create_user(self, email,  password=None):
        # extra_fields = yeni fields eklendiğinde onları da alıp flexible olur
        """"Creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email addresses')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,  password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom user model supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()  # creates new UserManager for our object

    USERNAME_FIELD = 'email'  # assign email as username for login

    def __str__(self):
        return self.email