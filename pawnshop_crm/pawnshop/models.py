from django.db import models


class Client(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100,
        null=False,
        blank=False
    )
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        null=False,
        blank=False
    )
    location = models.CharField(
        verbose_name='Населенный пункт',
        max_length=100,
        null=False,
        blank=False
    )
    street = models.CharField(
        verbose_name='Улица',
        max_length=100,
        null=False,
        blank=False
    )
    house_number = models.CharField(
        verbose_name='Номер дома',
        max_length=100,
        null=False,
        blank=False
    )
    apartment_number = models.CharField(
        verbose_name='Номер квартиры',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    actual_address = models.CharField(
        verbose_name='Фактический адрес проживания',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    birth_place = models.CharField(
        verbose_name='Место рождения',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=100,
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        null=False,
        blank=False
    )
    citizenship = models.CharField(
        verbose_name='Гражданство',
        max_length=100,
        null=False,
        blank=False
    )
    files = models.ImageField(
        verbose_name='Файлы',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ConfirmDocument(models.Model):
    client = models.OneToOneField(
        'pawnshop.Client',
        related_name='confirm_document',
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    document_type = models.CharField(
        verbose_name='Тип документа',
        max_length=100,
        null=False,
        blank=False
    )
    iin = models.CharField(
        verbose_name='ИИН',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )
    serial_number = models.CharField(
        verbose_name='Серийный номер',
        max_length=100,
        null=False,
        blank=False
    )
    given_by = models.CharField(
        verbose_name='Выдан кем',
        max_length=100,
        null=False,
        blank=False
    )
    given_at = models.DateField(
        verbose_name='Дата выдачи',
        null=False,
        blank=False
    )
    note = models.CharField(
        verbose_name='Примечание',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        verbose_name='Фотография документа',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Документ',
        verbose_name_plural = 'Документы'