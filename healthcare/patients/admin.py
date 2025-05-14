from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'blood_group', 'contact_number', 'user')
    list_filter = ('gender', 'blood_group', 'created_at')
    search_fields = ('first_name', 'last_name', 'contact_number', 'email')
    readonly_fields = ('created_at', 'updated_at')