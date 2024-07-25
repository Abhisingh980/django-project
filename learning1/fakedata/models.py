from django.db import models


# Create your models here.
class fakedata(models.Model):
    unique_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.first_name
