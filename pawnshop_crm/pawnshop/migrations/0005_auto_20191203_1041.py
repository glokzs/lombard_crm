# Generated by Django 2.1.11 on 2019-12-03 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0004_auto_20191104_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='loan',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
