# Generated by Django 5.0.1 on 2024-01-24 17:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='null', max_length=255, verbose_name='placeholder'),
            preserve_default=False,
        ),
    ]
