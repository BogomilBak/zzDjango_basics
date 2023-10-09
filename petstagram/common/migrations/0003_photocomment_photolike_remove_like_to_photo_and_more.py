# Generated by Django 4.2.1 on 2023-05-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_photo'),
        ('common', '0002_alter_comment_to_photo_alter_like_to_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='to_photo',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]