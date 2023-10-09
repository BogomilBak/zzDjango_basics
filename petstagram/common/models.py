from django.db import models

from photos.models import Photo

class PhotoComment(models.Model):
    text = models.TextField(
        max_length=300,
        blank=False,
        null=False,
    )
    date_time_of_publication = models.DateField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

class PhotoLike(models.Model):
    # field in relation is {NAME_OF_THIS_MODEL}_set
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )