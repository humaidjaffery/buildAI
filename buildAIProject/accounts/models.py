from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('To create an acocunt, you must have an email')

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        global superu 
        superu = True
        user = self.create_user(email=email, password=password)
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email           = models.CharField(max_length=30, unique=True, primary_key=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True