from django.db import models


class Operation(models.Model):
    TYPE_LOAN_CREATE = 'Добавление займа'
    TYPE_LOAN_BUYOUT = 'Выкуп займа'
    TYPE_LOAN_PROLONGATION = 'Пролонгация займа'

    STATUS_CHOICES = (
        (TYPE_LOAN_CREATE, 'Добавление займа'),
        (TYPE_LOAN_BUYOUT, 'Выкуп займа'),
        (TYPE_LOAN_PROLONGATION, ' Пролонгация займа'),
    )

    employee = models.ForeignKey(
        'auth.User',
        related_name='employee',
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        default=None
    )
    amount = models.DecimalField(
        verbose_name='Сумма операции',
        max_digits=20,
        decimal_places=10,
        null=False,
        blank=False,
        default=None
    )
    loan = models.ForeignKey(
        'pawnshop.Loan',
        related_name='operations',
        verbose_name='Займ',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        default=None
    )
    operation_type = models.CharField(
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
        return f'Залог #\'{self.pk},' \
            f'Тип операции: {self.operation_type}, ' \
            f'Сумма: {self.amount}, ' \
            f'Операция проведена: {self.created_at}\'' \
            f'Инициатор: {self.employee} '
