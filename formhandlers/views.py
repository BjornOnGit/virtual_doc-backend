from rest_framework import generics
from .models import BookAppointment, PatientInfo
from .serializers import BookAppointmentSerializer, PatientInfoSerializer

class BookAppointment(generics.CreateAPIView):
    queryset = BookAppointment.objects.all()
    serializer_class = BookAppointmentSerializer

book_appointment = BookAppointment.as_view()

class PatientInfo(generics.CreateAPIView):
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoSerializer

patient_info = PatientInfo.as_view()

# Create your views here.
