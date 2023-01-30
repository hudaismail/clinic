from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=250)
    doctor_email = models.CharField(max_length=250)
    doctor_phone = models.CharField(max_length=250)
    doctor_address = models.CharField(max_length=250)

    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    Patient_name = models.CharField(max_length=250)
    Patient_email = models.CharField(max_length=250)
    Patient_phone = models.CharField(max_length=250)
    Patient_address = models.CharField(max_length=250)

    def __str__(self):
        return self.Patient_name

class Meeting(models.Model):
    doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name= models.ForeignKey(Patient,on_delete=models.CASCADE)
    date        = models.DateField()
    hour        = models.TextField()

    def __str__(self):
        return f'{self.doctor_name} - {self.patient_name} - {self.date} - {self.hour}'

class Appointment(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    message= models.TextField(blank=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone} - {self.message} - {self.date}'


