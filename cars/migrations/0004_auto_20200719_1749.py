# Generated by Django 3.0.8 on 2020-07-19 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200719_1747'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cars',
            new_name='car',
        ),
    ]
