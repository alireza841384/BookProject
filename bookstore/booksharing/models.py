from django.db import models
from django.db import transaction , IntegrityError
from django.contrib.auth.models import User
import shortuuid

# Create your models here.

class ShareCode(models.Model):
    code=models.CharField(max_length=10,unique=True)
    # Shared_with=
    # blocked_with=

    def save(self, *args, **kwargs):
        if self.code:
            with transaction.atomic():
                while True:
                    self.code=shortuuid.ShortUUID.random(length=10)
                    try:
                        super().save(*args,**kwargs)
                        break
                    except IntegrityError:
                        continue
        else:
            super().save(*args,**kwargs)



class SharePanelControl(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='sharePanel')
    Access_to=models.ManyToManyField('self',symmetrical=False,related_name="followings")
    share_code=models.OneToOneField(ShareCode,on_delete=models.CASCADE)

