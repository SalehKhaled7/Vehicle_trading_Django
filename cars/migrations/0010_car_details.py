# Generated by Django 3.0.8 on 2020-07-29 21:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
