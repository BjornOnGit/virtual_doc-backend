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
        fields = ['age', 'weight', 'sex', 'height', 
                  'blood_pressure', 'temperature', 
                  'medical_history'
                ]

    def create(self, validated_data):
        appointment = BookAppointment.objects.last()
        if appointment is None:
            raise serializers.ValidationError("No appointment available")
        validated_data['appointment'] = appointment
        patient_info = PatientInfo.objects.create(**validated_data)
        return patient_info   
