from django.db import models

from web.validators import ValueInRangeValidator, validate_text

class Person(models.Model):
    name = models.CharField(
        max_length=20,
    )

    profile_image = models.ImageField(
        upload_to='persons/',
        null=True,
        blank=False
    )

class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3
    MAX_LENGTH_TEXT = 25
    text = models.CharField(
        max_length=MAX_LENGTH_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
