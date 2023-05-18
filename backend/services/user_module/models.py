from django.contrib.auth.models import AbstractUser
from django.db import models
from services.file_module.models import File
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        UserSettings.objects.get_or_create(user=self)

    def files(self):
        files = File.objects.filter(object_id=self.id,
                                    content_type_id=ContentType.objects.get_for_model(User).id)
        if files.exists():
            return files[0].absolute_file_url

        return None

    is_premium = models.BooleanField(default=False, verbose_name='Premium')


class UserSettings(models.Model):
    is_send_push = models.BooleanField(default=True, verbose_name='Send Push')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')
