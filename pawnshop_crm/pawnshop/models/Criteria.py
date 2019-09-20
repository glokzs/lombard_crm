from django.db import models


class Criteria(models.Model):
    category = models.ManyToManyField(
        'pawnshop.Category',
        related_name='criteries',
        verbose_name='Относится к категории'
    )
    name = models.CharField(
        verbose_name='Название критерия',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'

    def __str__(self):
        return self.name
