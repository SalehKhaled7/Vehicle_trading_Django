# Generated by Django 3.0.8 on 2020-07-31 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_auto_20200731_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('manual', 'MANUAL'), ('automatic', ' AUTOMATIC')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
