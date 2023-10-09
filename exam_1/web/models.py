from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_only_alphanumeric,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    GENRES = (('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'),
              ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music',),
              ('Country Music', 'Country Music',), ('Dance Music', 'Dance Music'),
              ('Hip Hop Music', 'Hip Hop Music',), ('Other', 'Other'))

    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    genre = models.CharField(
        blank=False,
        null=False,
        choices=GENRES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(0.0),
        ),
    )

    class Meta:
        ordering = ('pk',)
