from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    BookName = models.CharField(max_length=50)
    Chocies = {"c1": "Derama", "c2": 'Action',
               "c3": 'SienceFiction', "c4": 'Sience', "c5": "Story"}
    Title = models.CharField(max_length=40, choices=Chocies)
    Author = models.CharField(max_length=40)
    TimeCreated = models.DateTimeField(auto_now=True)
    Creator = models.ForeignKey(User, on_delete=models.CASCADE)
