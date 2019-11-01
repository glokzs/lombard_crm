from django.db import models

class Operation(models.Model):
    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='Дата создания'
    )
    username = models.CharField(
        verbose_name='Имя',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    description_operation = models.CharField(
        verbose_name='Описание операции',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    type_operation = models.CharField(
        verbose_name='Тип операции',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'Операция №\'{self.pk} {self.description_operation}\''
