from rest_framework.serializers import ModelSerializer

from storage.models import FileUpload


class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('hash', 'file', 'uploaded_at')
