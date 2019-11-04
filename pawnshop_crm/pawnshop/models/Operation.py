from django.db import models


class Operation(models.Model):
    STATUS_OPEN = 'Выдача заема'
    STATUS_CLOSED = 'Выкуп'
    STATUS_EXPIRED = 'Пролонгация'

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Выдача заема'),
        (STATUS_CLOSED, 'Выкуп'),
        (STATUS_EXPIRED, ' Пролонгация'),
    )
    username = models.ForeignKey(
        'accounts.Users',
        related_name='operation_user',
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None
    )
    amount = models.ForeignKey(
        'pawnshop.Loan',
        related_name='operation_amount',
        verbose_name='сумма по операции',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        default=0
    )
    ticket_number = models.ForeignKey(
        'pawnshop.Ticket',
        related_name='operation_ticket',
        verbose_name='номер билета',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None
    )
    type_operation = models.CharField(
        verbose_name='Статус',
        max_length=100,
        null=False,
        blank=False,
        default=None,
        choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'Операция №\'{self.pk},' \
            f'Тип операции: {self.type_operation}, ' \
            f'Билет№ {self.ticket_number}, ' \
            f'Сумма: {self.amount}, ' \
            f'Операция проведена: {self.created_at}\'' \
            f'Инициатор: {self.username} '
