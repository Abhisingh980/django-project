from enum import unique
from django.db import models
#import random

# Create your models here.
class fakedata(models.Model):
    unique_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.first_name
