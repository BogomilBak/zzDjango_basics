# Generated by Django 4.2.2 on 2023-06-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_person_todo_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
