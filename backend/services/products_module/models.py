from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    path = models.CharField(default=f'{title}', max_length=255, verbose_name='Path')
    image_path = models.CharField(default='', max_length=255, verbose_name='Image Path')
    description = models.TextField(max_length=2000, verbose_name='Description')


class UserHistoryUnit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='history')
    input = models.TextField(max_length=255, verbose_name='Input')
    result = models.CharField(max_length=255, verbose_name='Result')
