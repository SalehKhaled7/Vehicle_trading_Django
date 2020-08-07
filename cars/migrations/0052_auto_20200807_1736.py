# Generated by Django 3.0.8 on 2020-08-07 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0051_auto_20200807_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
        migrations.AlterField(
            model_name='image',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
