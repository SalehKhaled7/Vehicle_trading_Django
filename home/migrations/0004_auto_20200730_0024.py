# Generated by Django 3.0.8 on 2020-07-29 21:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200729_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='smtpemail',
            new_name='smtp_email',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='smtppassword',
            new_name='smtp_password',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='smtpport',
            new_name='smtp_port',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='smtpserver',
            new_name='smtp_server',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='aboutus',
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
