from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from storage.mixins import CreateRetrieveDestroyModelMixin
from storage.models import FileUpload
from storage.serializers import FileUploadSerializer
from storage.utils import is_directory_empty, remove_directory


class UploadViewSet(CreateRetrieveDestroyModelMixin,
                    viewsets.GenericViewSet):
    """
    Viewset that support only uploading, downloading and deleting files from storage
    """
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [FormParser, MultiPartParser]
    lookup_field = 'hash'

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        return redirect(obj)

    def perform_destroy(self, instance):
        instance.delete()
        path_to_file = instance.file.path
        instance.file.delete(save=False)
        if is_directory_empty(path_to_file):
            remove_directory(path_to_file)
