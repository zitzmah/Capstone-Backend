from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    dateOfBirth=models.DateField()
    sex=models.CharField(max_length=100)
    mrn=models.IntegerField()

    def __str__(self):
        return self.name

class BBTest(models.Model):
    patient = models.ForeignKey(Patient, related_name='bbtests', on_delete=models.CASCADE, null=True)
    test_name = models.CharField(max_length=600)
    result = models.CharField(max_length=600)
    test_date = models.DateField()

    def __str__(self):
        return f"{self.patient.name}'s {self.test.name} Test"

    def save(self, *args, **kwargs):
        self.patient = kwargs.pop('patient', None)
        super().save(*args, **kwargs)

class BloodUnit(models.Model):
    patient = models.ForeignKey(Patient, related_name='blood_units', on_delete=models.CASCADE, null=True)
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    unit_number = models.CharField(max_length=20, unique=True)
    blood_group = models.CharField(max_length=3, choices=blood_group_choices)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Blood Unit {self.unit_number} for {self.patient.name}"

    def save(self, *args, **kwargs):
        self.patient = kwargs.pop('patient', None)
        super().save(*args, **kwargs)
