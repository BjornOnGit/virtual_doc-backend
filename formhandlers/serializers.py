from rest_framework import serializers
from .models import BookAppointment, PatientInfo

class BookAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAppointment
        fields = '__all__'

class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'
