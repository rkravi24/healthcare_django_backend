from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'license_number', 'contact_number', 'user')
    list_filter = ('specialization', 'gender', 'created_at')
    search_fields = ('first_name', 'last_name', 'specialization', 'license_number', 'contact_number', 'email')
    readonly_fields = ('created_at', 'updated_at')