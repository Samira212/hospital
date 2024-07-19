from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import UserProfileFilter


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'doctor']
    filterset_class = UserProfileFilter

class DoctorViewSets(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class MedicalRecordViewSets(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class AppointmentViewSets(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class MedicationViewSets(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class FitnessProgramViewSets(viewsets.ModelViewSet):
    queryset = FitnessProgram.objects.all()
    serializer_class = FitnessProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
