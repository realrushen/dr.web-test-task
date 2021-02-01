from rest_framework import exceptions
from rest_framework.status import HTTP_400_BAD_REQUEST


class UniqueConstraintError(exceptions.ValidationError):
    default_detail = 'This file already exists in storage'
    default_code = 'not_unique'
