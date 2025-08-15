from django.db import models
from django.db import transaction , IntegrityError
from django.contrib.auth.models import User
import shortuuid

# Create your models here.


class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    position=models.CharField()

    def changePossitio(newPosiitio):
        pass



class Group(models.Model):
    Owner=models.ForeignKey(User)
    name=models.CharField(max_length=20)
    description=models.TextField(max_length=50,blank=True)
    members=models.ManyToManyField(Member)
    timeCreated=models.DateTimeField(auto_now=True)


class Message(models.Model):
   creator=models.ForeignKey(User)
   text=models.TextField()
   time=models.DateTimeField(auto_now=True)
   group=models.ForeignKey()








