from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # TODO додати створення налаштувань у методі save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        UserSettings.objects.get_or_create(user=self)


class UserAddress(models.Model):
    country = models.CharField(max_length=255, verbose_name='Country')
    city = models.CharField(max_length=255, verbose_name='City')
    address = models.CharField(max_length=255, verbose_name='Address')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_address')


class UserSettings(models.Model):
    is_send_push = models.BooleanField(default=True, verbose_name='Send Push')
    is_premium = models.BooleanField(default=False, verbose_name='Premium')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')
