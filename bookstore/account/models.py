from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    firstName = models.CharField(max_length=20, blank=True, null=True)
    lastName = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender_choices = {"male": "male", "female": "female"}
    gender = models.CharField(choices=gender_choices,  blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

# Create your models here.
