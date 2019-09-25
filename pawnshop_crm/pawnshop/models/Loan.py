from django.db import models


class Loan(models.Model):
    client = models.ForeignKey(
        'pawnshop.Client',
        related_name='loans',
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    pledge_item = models.ForeignKey(
        'pawnshop.PledgeItem',
        related_name='loan',
        null=False,
        blank=False,
        default=None,
        verbose_name='Предмет залога',
        on_delete=models.CASCADE
    )
    client_amount = models.DecimalField(
        verbose_name='Запрашиваемая сумма',
        max_digits=10,
        decimal_places=2,
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
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        verbose_name = 'Сумма займа',
        verbose_name_plural = 'Суммы займа'

    def __str__(self):
        return f'{self.client} - {self.client_amount} ({self.total_amount})'
