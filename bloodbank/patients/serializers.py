from .models import Patient, BBTest, BloodUnit
from rest_framework import serializers

class BBTestSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)
    class Meta:
        model=BBTest
        fields = "__all__"

class BloodUnitSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)
    class Meta:
        model=BloodUnit
        fields = "__all__"

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    bbtests = BBTestSerializer(many=True, read_only=False)
    blood_units = BloodUnitSerializer(many=True, read_only=False)

    class Meta:
        model=Patient
        fields = ['id', 'name', 'dateOfBirth', 'sex', 'mrn', 'bbtests', 'blood_units']