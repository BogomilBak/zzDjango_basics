from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def capitalized_first_name(value):
    if not value == value.capitalize():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_name_validator(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
        ]
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            capitalized_first_name
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            capitalized_first_name
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    PLANT_TYPE_CHOICES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=14,
        choices=PLANT_TYPE_CHOICES
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            MinLengthValidator(2),
            only_letters_name_validator
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

    price = models.FloatField(
        blank=False,
        null=False,
    )






