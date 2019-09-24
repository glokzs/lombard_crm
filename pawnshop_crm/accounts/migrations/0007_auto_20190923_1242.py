# Generated by Django 2.1.5 on 2019-09-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190921_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default='Test', max_length=30, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Administrator', 'Administrator'), ('Cashier', 'Cashier'), ('Auditor', 'Auditor')], default='Auditor', max_length=1, verbose_name='Тип прав'),
        ),
    ]