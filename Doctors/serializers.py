from rest_framework import serializers

from Doctors.models import Doctor, Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    specializations = SpecializationSerializer(many=True)
    work_experience = serializers.IntegerField(read_only=True)
