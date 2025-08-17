from django.db import models
from django.db import transaction , IntegrityError
from django.contrib.auth.models import User
import shortuuid

# Create your models here.





class Group(models.Model):
    Owner=models.ForeignKey(User)
    name=models.CharField(max_length=20)
    description=models.TextField(max_length=50,blank=True)
    timeCreated=models.DateTimeField(auto_now=True)


        

class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    groups=models.ForeignKey(Group,related_name='members')
    position=models.CharField()

    def changePossitio(newPosiitio):
        pass


class Message(models.Model):
   creator=models.ForeignKey(User)
   text=models.TextField()
   time=models.DateTimeField(auto_now=True)
   group=models.ForeignKey()






