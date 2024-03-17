from django.urls import path
from . import views

urlpatterns = [
    path('diseases/', views.diseases, name='diseases'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('chatbot/', views.ChatBotView.as_view(), name='chatbot'),
]