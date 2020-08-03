# Generated by Django 3.0.8 on 2020-08-03 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='05---------', max_length=20)),
                ('address', models.CharField(blank=True, default='default_address', max_length=150)),
                ('city', models.CharField(default='default_city', max_length=20)),
                ('country', models.CharField(default='default_country', max_length=20)),
                ('image', models.ImageField(default='images/users/default_user.jpg', upload_to='images/users/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]