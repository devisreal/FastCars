# Generated by Django 4.0.6 on 2022-08-16 10:46

import cloudinary.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastcars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='image'),
        ),
    ]
