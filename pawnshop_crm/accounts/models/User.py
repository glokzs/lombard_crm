from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    initial_password_changed_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Пароль изменен')
