from django.db import models


class FakeOperation(models.Model):
    client = models.ForeignKey(
        'pawnshop.Client',
        related_name='fake_operations',
        null=False,
        blank=False,
        default=None,
        required=True,
        verbose_name='Относится к клиентам',
        on_delete=models.CASCADE
    )
    pledge_item = models.ForeignKey(
        'pawnshop.PledgeItem',
        related_name='fake_operations',
        null=False,
        blank=False,
        default=None,
        required=True,
        verbose_name='Относится к залоговому имуществу',
        on_delete=models.CASCADE
    )
    note = models.TextField(
        verbose_name='Описание фейк операции',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )