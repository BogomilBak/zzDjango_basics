# Generated by Django 4.2.1 on 2023-05-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, null=True, to='pets.pet'),
        ),
    ]