from django.contrib import admin
from .models import Symptom, Disease

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_symptoms')

    def display_symptoms(self, obj):
        return ", ".join([symptom.name for symptom in obj.symptoms.all()])
    display_symptoms.short_description = 'Symptoms'

admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Disease, DiseaseAdmin)

# Register your models here.
