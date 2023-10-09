# Generated by Django 4.2.3 on 2023-07-07 16:37

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), web.models.capitalize_validator])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), web.models.capitalize_validator])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
