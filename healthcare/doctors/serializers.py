from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 'first_name', 'last_name', 'specialization', 
            'license_number', 'gender', 'contact_number', 'email', 
            'address', 'years_of_experience', 'consultation_fee', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def create(self, validated_data):
        # Associate the doctor with the authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)