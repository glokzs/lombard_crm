from django.db import models


class ConfirmDocument(models.Model):
    client = models.OneToOneField(
        'pawnshop.Client',
        related_name='confirm_document',
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    document_type = models.CharField(
        verbose_name='Тип документа',
        max_length=100,
        null=False,
        blank=False
    )
    iin = models.CharField(
        verbose_name='ИИН',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )
    serial_number = models.CharField(
        verbose_name='Серийный номер',
        max_length=100,
        null=False,
        blank=False
    )
    given_by = models.CharField(
        verbose_name='Выдан кем',
        max_length=100,
        null=False,
        blank=False
    )
    given_at = models.DateField(
        verbose_name='Дата выдачи',
        null=False,
        blank=False
    )
    note = models.CharField(
        verbose_name='Примечание',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        verbose_name='Фотография документа',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Документ',
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.client} - {self.document_type} ({self.iin})'
