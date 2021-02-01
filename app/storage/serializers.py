from rest_framework import serializers

from storage.models import FileUpload


class FileUploadSerializer(serializers.Serializer):
    hash = serializers.CharField(max_length=64, min_length=64, allow_null=True, required=False)

    def create(self, validated_data):
        return FileUpload.objects.create(file=self.initial_data.get('file'))
