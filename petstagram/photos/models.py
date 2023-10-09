from django.db import models
from django.core.validators import MinLengthValidator

from pets.models import Pet
from photos.validators import validate_file_size_greater_than_5mb

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(validate_file_size_greater_than_5mb,),
        null=False,
        blank=True,
    )
    description = models.TextField(
        validators=(MinLengthValidator(10),),
        max_length=300,
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )


    