from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def capitalize_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validator_only_letters_in_name(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            MinLengthValidator(2),
            capitalize_validator,
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(1),
            capitalize_validator,
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40,
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ]
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        default=18,
        blank=True,
        null=True,
    )


class Fruit(models.Model):
    name = models.CharField(
        blank=False,
        null=False,

        max_length=30,
        validators=[
            MinLengthValidator(2),
            validator_only_letters_in_name,
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
    )


