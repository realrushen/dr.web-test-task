from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import validators

from storage.exeptions import UniqueConstraintError
from storage.utils import custom_path_handler, generate_hash


class FileUpload(models.Model):
    original_name = models.CharField(max_length=255, blank=True, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(upload_to=custom_path_handler)
    hash = models.CharField(max_length=255, unique=True, blank=True)
    directory = models.CharField(max_length=2, blank=True, editable=False)

    def __str__(self):
        return f'{self.original_name}, uploaded: {self.uploaded_at}, pk: {self.pk}'

    def save(self, *args, **kwargs):
        try:
            self.clean_fields()
        except ValidationError as e:
            raise validators.ValidationError({field: value for field, value in e.message_dict.items()})
        if not self.id:
            bytes_like_object = self.file.read()
            self.hash = generate_hash(bytes_like_object)
            self.directory = self.hash[:2]
            self.original_name = self.file.name
            try:
                self.validate_unique()
            except ValidationError:
                raise UniqueConstraintError

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return self.file.url
