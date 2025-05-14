from rest_framework import serializers
from .models import Patient
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated


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
    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]  #access by only authenticated users

    def perform_create(self, serializer):
        #Automatically associate the patient with the authenticated user
        serializer.save(user=self.request.user)
