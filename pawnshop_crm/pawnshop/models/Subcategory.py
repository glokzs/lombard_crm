from django.db import models


class Subcategory(models.Model):
    category = models.ForeignKey(
        'pawnshop.Category',
        related_name='subcategories',
        null=True,
        blank=True,
        default=None,
        verbose_name='Родительская категория',
        on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        'pawnshop.Subcategory',
        related_name='subcategories',
        null=True,
        blank=True,
        default=None,
        verbose_name='Родительская субкатегория',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Имя подкатегории',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
