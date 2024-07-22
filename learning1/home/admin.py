from django.contrib import admin
from .models import Student, demo

# Register your models here.
# Registering the model in the admin panel

admin.site.register(Student)

admin.site.register(demo)
