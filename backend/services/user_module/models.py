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

    is_premium = models.BooleanField(default=False, verbose_name='Premium')


class UserSettings(models.Model):
    is_send_push = models.BooleanField(default=True, verbose_name='Send Push')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')
