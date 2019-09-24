# Generated by Django 2.1.5 on 2019-09-24 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0011_auto_20190921_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_amount', models.DecimalField(decimal_places=2, default=None, max_digits=10, verbose_name='Запрашиваемая сумма')),
                ('duration', models.IntegerField(default=5, verbose_name='Период')),
                ('date_of_expire', models.DateTimeField(max_length=100, verbose_name='Срок погашения займа')),
                ('total_amount', models.DecimalField(decimal_places=2, default=None, max_digits=10, verbose_name='Итоговая сумма кредита')),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='pawnshop.Client', verbose_name='Клиент')),
                ('pledge_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='pawnshop.PledgeItem', verbose_name='Предмет залога')),
            ],
            options={
                'verbose_name': ('Сумма займа',),
                'verbose_name_plural': 'Суммы займа',
            },
        ),
    ]