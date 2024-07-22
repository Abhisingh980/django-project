from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
class Fooddata(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    foodname = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.foodname
