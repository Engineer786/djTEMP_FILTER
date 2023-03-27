from django.db import models

# Create your models here.
class Manager(models.Model):
    name=models.CharField(max_length=30)
    sal=models.FloatField()
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=30)