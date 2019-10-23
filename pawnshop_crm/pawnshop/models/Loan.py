from django.db import models


class Loan(models.Model):
    STATUS_OPEN = 'Открыт'
    STATUS_CLOSED = 'Закрыт'
    STATUS_EXPIRED = 'Истек'

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Открыт'),
        (STATUS_CLOSED, 'Закрыт'),
        (STATUS_EXPIRED, 'Истек'),
    )

    client = models.ForeignKey(
        'pawnshop.Client',
        related_name='loans',
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    client_amount = models.DecimalField(
        verbose_name='Запрашиваемая сумма',
        max_digits=20,
        decimal_places=10,
        null=False,
        blank=False,
        default=None
    )
    duration = models.IntegerField(
        verbose_name='Период',
        default=5,
        null=False,
    )
    date_of_expire = models.DateTimeField(
        verbose_name='Срок погашения займа',
        max_length=100,
        null=False,
        blank=False
    )
    total_amount = models.DecimalField(
        verbose_name='Итоговая сумма кредита',
        max_digits=20,
        decimal_places=10,
        null=False,
        blank=False,
        default=None
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=100,
        null=False,
        blank=False,
        default=None,
        choices=STATUS_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания')

    class Meta:
        verbose_name = 'Займ',
        verbose_name_plural = 'Займы'

    def __str__(self):
        return f'{self.client} - {self.client_amount} ({self.total_amount})'
