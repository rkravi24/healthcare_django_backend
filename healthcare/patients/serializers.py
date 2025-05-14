from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 
            'gender', 'blood_group', 'contact_number', 'email', 
            'address', 'medical_history', 'allergies', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def create(self, validated_data):
        #associate the patient with the authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)