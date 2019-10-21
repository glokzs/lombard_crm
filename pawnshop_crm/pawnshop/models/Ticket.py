from django.db import models


class Ticket(models.Model):
    loan = models.OneToOneField(
        'pawnshop.Loan',
        related_name='ticket',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        verbose_name='Залог'
    )
    file_name = models.CharField(
        max_length=100,
        verbose_name='Имя файла',
        null=False,
        blank=False,
        default=None
    )
    file_path = models.CharField(
        max_length=100,
        verbose_name='Путь к файлу',
        null=False,
        blank=False,
        default=None
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.file_name
