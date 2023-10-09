#pets/models.py
from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=False,
        null=False,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.name}")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name