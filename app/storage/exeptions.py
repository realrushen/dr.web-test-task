from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST


class UniqueConstraintError(ValidationError):
    default_detail = 'Unique constraint failed'
    default_code = HTTP_400_BAD_REQUEST
