import os
from django.core.exceptions import ValidationError
from tint_django.settings import VALID_FILE_TYPES


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = VALID_FILE_TYPES
    if not ext.upper() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
