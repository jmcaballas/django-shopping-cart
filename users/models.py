from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    billing_street = models.CharField(max_length=50)
    billing_city = models.CharField(max_length=50)
    billing_postal = models.CharField(max_length=50)
    shipping_street = models.CharField(max_length=50)
    shipping_city = models.CharField(max_length=50)
    shipping_postal = models.CharField(max_length=50)
    phone = models.CharField(help_text='Enter 11-digit phone number', max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
