from rest_framework import generics
from .models import BookAppointment, PatientInfo, BookNow
from .serializers import BookAppointmentSerializer, PatientInfoSerializer, BookNowSerializer

class BookAppointment(generics.CreateAPIView):
    queryset = BookAppointment.objects.all()
    serializer_class = BookAppointmentSerializer

book_appointment = BookAppointment.as_view()

class BookNow(generics.CreateAPIView):
    queryset = BookNow.objects.all()
    serializer_class = BookNowSerializer

book_now = BookNow.as_view()

class PatientInfo(generics.CreateAPIView):
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoSerializer

patient_info = PatientInfo.as_view()

# Create your views here.
