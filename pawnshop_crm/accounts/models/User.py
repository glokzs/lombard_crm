from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, verbose_name='Пользователь')

    email = models.EmailField(
        unique=True)

    initial_password_changed_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Пароль изменен')

    middle_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="Test",
        verbose_name='Отчество'
    )

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
                ('add_user', 'Добавление пользователей'),
                ('add_loan', 'Добавление займа'),
            )
