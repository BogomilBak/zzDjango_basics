# Generated by Django 4.2.1 on 2023-05-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_employee_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('jr', 'Junior'), ('reg', 'Regular'), ('sr', 'Senior')], max_length=25, verbose_name='Seniority level'),
        ),
    ]