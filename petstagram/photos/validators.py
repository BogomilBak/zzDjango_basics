from django.forms import ValidationError


def validate_file_size_greater_than_5mb(image_object):
    if image_object.size > 5 * 1024 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")