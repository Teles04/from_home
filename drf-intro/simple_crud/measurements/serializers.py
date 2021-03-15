from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude',


class MeasurementSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField()

    class Meta:
        model = Measurement
        fields = 'value', 'created_at', 'updated_at', 'project_id',

    def create(self, validated_data):
        project_data = validated_data.pop('project_id')
        measurement = Measurement.objects.create(**validated_data, project_id=project_data)
        measurement.save()
        return measurement








