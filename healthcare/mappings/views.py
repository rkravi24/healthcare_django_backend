from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingDetailSerializer
from patients.models import Patient


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PatientDoctorMappingDetailSerializer
        return PatientDoctorMappingSerializer

    def get_queryset(self):
        # Return mappings for patients created by the current user
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        #only allow updates for mappings of patients belonging to the authenticated user
        if instance.patient.user != request.user:
            return Response(
                {"detail": "You do not have permission to update this mapping."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #only allow deletion for mappings of patients belonging to the authenticated user
        if instance.patient.user != request.user:
            return Response(
                {"detail": "You do not have permission to delete this mapping."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_by_patient(self, request, patient_id=None):
        """
        Get all doctors assigned to a specific patient
        """
        try:
            #verify the patient belongs to the current user
            patient = Patient.objects.get(id=patient_id, user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {"detail": "Patient not found or you don't have permission to access this patient."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = PatientDoctorMappingDetailSerializer(mappings, many=True)
        
        return Response(serializer.data)