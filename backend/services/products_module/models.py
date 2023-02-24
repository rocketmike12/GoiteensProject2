from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    path = models.CharField(default=f'{title}', max_length=255, verbose_name='Path')
    image_path = models.CharField(default='', max_length=255, verbose_name='Image Path')
    description = models.TextField(max_length=2000, verbose_name='Description')
