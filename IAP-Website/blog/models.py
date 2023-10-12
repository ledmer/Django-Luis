from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime 

class Post(models.Model):
    title = models.CharField(max_length=20)
    current_time = models.DateTimeField(default=timezone.now, blank=True)
    body = models.CharField(max_length=1000000)


# Create your models here.
