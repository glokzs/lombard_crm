from django.db import models


class Contract(models.Model):
    open_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата открытия кредита',
        null=False,
        blank=False
    )
    loan = models.OneToOneField(
        'pawnshop.Loan',
        related_name='contract_loan',
        on_delete=models.PROTECT,
        verbose_name='кредит',
        null=False,
        blank=False,
        default=None
    )

    ticket_number = models.OneToOneField(
        'pawnshop.Contract',
        related_name='contract',
        on_delete=models.CASCADE,
        verbose_name='номер залогового билета',
        null=False,
        blank=False,
        default=None
    )
    client = models.OneToOneField(
        'pawnshop.Client',
        related_name='contracts',
        on_delete=models.PROTECT,
        verbose_name='клиент',
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        verbose_name = 'Залоговый билет'
        verbose_name_plural = 'залоговые билеты'

    # def __str__(self):
    #     return f'Залоговый билет № {self.ticket_number}'
