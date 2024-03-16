from django.urls import path
from . import views

urlpatterns = [
    path('labs/', views.lab_location, name='labs'),
    path('pharmacies/', views.pharmacy_location, name='pharmacies'),
]