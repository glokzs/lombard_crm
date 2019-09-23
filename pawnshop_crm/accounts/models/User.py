from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = (
    ("Administrator", "Administrator"),
    ("Cashier", "Cashier"),
    ("Auditor", "Auditor"),
    )

class User(AbstractUser):
    initial_password_changed_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Пароль изменен')
    middle_name = models.CharField(
        max_length=30,
        null = True,
        blank=True,
        default = None,
        verbose_name='Отчество'
    )
    user_type = models.CharField(
        max_length= 1,
        null = False,
        blank = False,
        default = None,
        choices= USER_TYPE_CHOICES,
        verbose_name='тип прав'
    )
