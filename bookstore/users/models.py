from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users.images', null=True,
                              blank=True, verbose_name='Изображение')
