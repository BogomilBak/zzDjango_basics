# Generated by Django 4.2.1 on 2023-05-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee_last_name_employee_years_of_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
