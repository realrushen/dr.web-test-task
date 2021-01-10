from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from storage.models import FileUpload


class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('hash', 'file', 'original_name')
