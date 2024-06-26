# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class TaxiDriver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
    taxi_number = models.CharField(max_length=100)
    phone = models.CharField(max_length=255)

    # Add other fields as necessary

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # Add other fields as necessary