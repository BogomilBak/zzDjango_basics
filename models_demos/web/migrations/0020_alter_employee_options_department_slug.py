# Generated by Django 4.2.1 on 2023-05-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_category_parent_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['age']},
        ),
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='dep-1', unique=True),
            preserve_default=False,
        ),
    ]
