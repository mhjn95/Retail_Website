from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Rfq(models.Model):
    file = models.FileField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    process = models.TextField(blank=True,null=True)
    material = models.TextField(blank=True,null=True)
    adddetails = models.TextField(blank=True,null=True)
    quality = models.IntegerField(blank=True,null=True)
    nearestloc = models.IntegerField(blank=True,null=True)
    leadtime = models.IntegerField(blank=True,null=True)
    pricing = models.IntegerField(blank=True,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)
    is_done = models.BooleanField(default=True)
    unique_id = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user_id.username
