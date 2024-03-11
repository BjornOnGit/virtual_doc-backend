from django.db import models

class BookAppointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    service_selected = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PatientInfo(models.Model):
    appointment = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    blood_pressure = models.CharField(max_length=10)
    temperature = models.IntegerField()
    medical_history = models.TextField()

    def __str__(self):
        return self.appointment.name
# Create your models here.
