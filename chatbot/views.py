from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
from django.conf import settings
from django.db import models
from django.db.models import Count
from .models import Symptom, Disease
from .serializers import SymptomSerializer, DiseaseSerializer

class SymptomView(APIView):
    def get(self, request, format=None):
        symptoms = Symptom.objects.all()
        serializer = SymptomSerializer(symptoms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

symptoms = SymptomView.as_view()
class DiseaseView(APIView):
    def get(self, request, format=None):
        diseases = Disease.objects.all()
        serializer = DiseaseSerializer(diseases, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

diseases = DiseaseView.as_view()

class ChatBotView(APIView):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    def symptom_checker(self, symptoms):
        # Get all diseases that have at least 4 of the symptoms
        diseases = Disease.objects.annotate(matching_symptoms=Count('symptoms', filter=models.Q(symptoms__name__in=symptoms)))
        diseases = diseases.filter(matching_symptoms__gte=4)
        return diseases

    def post(self, request, format=None):
        user_message = request.data.get('message', None)
        
        if user_message is None:
            return Response({"error": "No message provided"}, status=400)
        
        #print(f"User's message: {user_message}")  # Print user's message to the console
        
        # Process user_message with OpenAI API
        response = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        # Get all symptoms from your database
        all_symptoms = Symptom.objects.all()

        #print(f"All symptoms: {[symptom.name for symptom in all_symptoms]}")  # Print all symptoms to the console

        # Check if each symptom is mentioned in the user's message
        mentioned_symptoms = [symptom.name.strip() for symptom in all_symptoms if symptom.name.strip().lower() in user_message.lower()]

        #print(f"Mentioned symptoms: {mentioned_symptoms}")  # Print mentioned symptoms to the console

        # Use symptom_checker to get a list of potential diagnoses
        diseases = self.symptom_checker(mentioned_symptoms)

        return Response({"diagnoses": [disease.name for disease in diseases]})

chatbot = ChatBotView.as_view()

        

# Create your views here.
