from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime 

class Post(models.Model):
    title = models.CharField(max_length=100)
    current_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploaded/galleries', blank=True, null=True)
    body = models.TextField()

    class Meta:
        ordering = ('-current_time',)
    
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    current_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        ordering = ('-current_time',)


# Create your models here.
