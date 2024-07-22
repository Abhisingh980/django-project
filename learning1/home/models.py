
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/images/',null=True, blank=True)
    file = models.FileField(upload_to='files/',null=True, blank=True)

class demo(models.Model):
    pass
