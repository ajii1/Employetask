from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.PositiveIntegerField()
    designation = models.CharField(max_length=40,default="")
    address = models.CharField(max_length=200)
