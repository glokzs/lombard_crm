# Generated by Django 2.1.5 on 2019-09-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_initial_password_changed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='initial_password_changed_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Пароль изменен'),
        ),
    ]
