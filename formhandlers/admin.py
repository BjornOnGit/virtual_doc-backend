from django.contrib import admin
from .models import BookAppointment, PatientInfo

class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 
        'scheduled_date', 'scheduled_time', 
        'service_selected'
    )

class PatientInfoAdmin(admin.ModelAdmin):
    list_display = (
        'appointment', 'age', 'weight', 
        'height', 'blood_pressure', 
        'temperature', 'medical_history'
    )

admin.site.register(BookAppointment, BookAppointmentAdmin)
admin.site.register(PatientInfo, PatientInfoAdmin)

# Register your models here.
