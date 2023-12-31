# Generated by Django 4.2.1 on 2023-05-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('works_full_time', models.BooleanField()),
                ('photo', models.URLField()),
            ],
        ),
    ]
