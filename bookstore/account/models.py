from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True)
    gender_choices = {"male": "male", "female": "female"}
    gender = models.CharField(choices=gender_choices, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

# Create your models here.
