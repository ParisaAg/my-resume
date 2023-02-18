from django.db import models

import datetime


# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title




class contact(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField()
    subject= models.CharField(max_length=255)
    text= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
