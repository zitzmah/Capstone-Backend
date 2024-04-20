from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    dateOfBirth=models.DateField()
    sex=models.CharField(max_length=100)
    mrn=models.IntegerField()
    bloodType=models.CharField(max_length=3, default='')
    antibodyScreen=models.CharField(max_length=20, default='')
    antibodyID=models.CharField(max_length=50, default='')