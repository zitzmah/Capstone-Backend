from .models import Patient, BBTest, BloodUnit
from rest_framework import permissions, viewsets
from .serializers import PatientSerializer, BBTestSerializer, BloodUnitSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    permission_classes=[permissions.AllowAny]

class TestViewSet(viewsets.ModelViewSet):
    queryset=BBTest.objects.all()
    serializer_class=BBTestSerializer
    permission_classes=[permissions.AllowAny]

class BloodUnitViewSet(viewsets.ModelViewSet):
    queryset=BloodUnit.objects.all()
    serializer_class=BloodUnitSerializer
    permission_classes=[permissions.AllowAny]