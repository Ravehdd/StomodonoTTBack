from rest_framework import serializers
from .models import *


class IndexSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source="patient.name")
    phone = serializers.CharField(source="patient.phone")
    personal_account = serializers.CharField(source="patient.personal_account")
    family_account = serializers.CharField(source="patient.family_account")

    clinic = serializers.CharField(source="clinic.name")
    doctor_name = serializers.CharField(source="doctor.name")

    class Meta:
        model = Patient
        fields = ("id", "add_time", "start_time", "end_time",
                  "cancel_time", "clinic", "doctor_name", "patient_id",
                  "patient", "phone", "personal_account", "family_account", "days_count")
