from django.db import models
import datetime

from django.utils.safestring import mark_safe


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Category(models.Model):
    Status = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=Status)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class car(models.Model):
    Status = (
        ('True', 'Yes'),
        ('False', 'NO'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=Status)
    photo = models.ImageField(blank=True, upload_to='images/')
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year_of_production = models.IntegerField('year', choices=year_choices(), default=current_year())
    engine_capacity = models.IntegerField()
    color = models.CharField(max_length=30)
    price = models.FloatField()
    doors = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.photo.url))

    image_tag.short_description = 'Image'


class Image(models.Model):
    cars = models.ForeignKey(car, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
