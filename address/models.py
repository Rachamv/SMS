from django.db import models
from django.contrib.auth.models import User


class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    emergency_contact = models.OneToOneField(EmergencyContact, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Address"
