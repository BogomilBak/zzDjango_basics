# Generated by Django 4.2.1 on 2023-05-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos'),
        ),
    ]