from rest_framework import serializers
from .models import BookAppointment, PatientInfo, BookNow

class BookAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAppointment
        fields = '__all__'

class BookNowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNow
        fields = '__all__'

class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'
