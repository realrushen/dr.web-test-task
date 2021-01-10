from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from storage.models import FileUpload
from storage.serializers import FileUploadSerializer
from storage.utils import is_directory_empty, remove_directory


class FileUploadViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing FileUpload instances.
    """
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class UploadViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
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
