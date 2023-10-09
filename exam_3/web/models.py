from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[
            MinLengthValidator(2, "The username must be a minimum of 2 chars")
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(18)
        ]
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPE_CHOICES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    car_type = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        choices=CAR_TYPE_CHOICES,
        verbose_name='Type',
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            MinLengthValidator(2)
        ],
    )

    year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1980, "Year must be between 1980 and 2049"),
            MaxValueValidator(2049, "Year must be between 1980 and 2049"),
        ],
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1.00),
        ],
    )