# Generated by Django 4.2.1 on 2023-05-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_employee_project_employeesprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.employee')),
            ],
        ),
    ]