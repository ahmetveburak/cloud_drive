from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def file_size_validator(file_object):
    MAX_UPLOAD_SIZE = 2621440
    file_size = file_object.file.size
    if file_size > MAX_UPLOAD_SIZE:
        file_size = file_size / (2 ** 20)
        raise ValidationError(_(f"File size should be less then 2.5MB. Current file size: {file_size:.2f}MB"))
