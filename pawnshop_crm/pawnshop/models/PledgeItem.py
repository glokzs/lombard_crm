from django.db import models


class PledgeItem(models.Model):
    category = models.ForeignKey(
        'pawnshop.Category',
        related_name='pledge_items',
        null=False,
        blank=False,
        default=None,
        verbose_name='Относится к категории',
        on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        'pawnshop.Subcategory',
        related_name='pledge_items',
        null=False,
        blank=False,
        default=None,
        verbose_name='Относится к подкатегории',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )
    price = models.DecimalField(
        verbose_name='Оценочная стоимость',
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=None
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        null=False,
        blank=False,
        default=None
    )
    note = models.CharField(
        verbose_name='Примечание',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        verbose_name='Фотография',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Предмет залога'
        verbose_name_plural = 'Предметы залога'


