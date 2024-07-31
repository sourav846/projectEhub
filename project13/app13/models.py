from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class profile(models.Model):
    Name=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)

class Movies(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=1000 , blank=True ,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Rate = models.FloatField(max_length=11)
    Uuid = models.UUIDField(default=uuid.uuid4)
    File = models.FileField(upload_to='video')
    Image = models.ImageField(upload_to='img')
    poster = models.ImageField(upload_to='poster')
