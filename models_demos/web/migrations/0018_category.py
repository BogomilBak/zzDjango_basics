# Generated by Django 4.2.1 on 2023-05-15 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_remove_acesscard_id_alter_acesscard_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
        ),
    ]