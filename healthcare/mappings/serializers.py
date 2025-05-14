from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'notes', 'created_at']
        read_only_fields = ['created_at']

    def validate(self, attrs):
        # Check if the patient belongs to the current user
        patient = attrs.get('patient')
        request = self.context.get('request')
        
        if patient.user != request.user:
            raise serializers.ValidationError({
                'patient': "You can only assign doctors to your own patients."
            })
        
        return attrs


class PatientDoctorMappingDetailSerializer(PatientDoctorMappingSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)