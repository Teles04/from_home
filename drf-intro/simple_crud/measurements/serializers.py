from rest_framework import serializers

from measurements.models import Project, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = 'id', 'value', 'created_at', 'updated_at',


class ProjectSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at', 'measurements',

    def create(self, validated_data):
        measurements_data = validated_data.pop('measurements')
        project = Project.objects.create(**validated_data)
        for measurement_data in measurements_data:
            Measurement.objects.create(project=project, **measurement_data)
        return project


