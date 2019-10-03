from django.db import models


class CriteriaValue(models.Model):
    criteria = models.ForeignKey(
        'pawnshop.Criteria',
        related_name='criteria_values',
        on_delete=models.CASCADE,
        verbose_name='Критерий',
        null=False,
        blank=False,
        default=None
    )
    pledge_item = models.ForeignKey(
        'pawnshop.PledgeItem',
        related_name='criteria_values',
        on_delete=models.CASCADE,
        verbose_name='Залоговое имущество',
        null=False,
        blank=False,
        default=None
    )
    value = models.CharField(
        max_length=100,
        verbose_name='Значение',
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f'{self.pledge_item.name} - {self.criteria.name} - {self.value}'

    class Meta:
        verbose_name = 'Значение критерия'
        verbose_name_plural = 'Значения критерия'
