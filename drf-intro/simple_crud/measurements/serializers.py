from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    measurements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at', 'measurements',

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = 'id', 'value', 'created_at', 'updated_at',
