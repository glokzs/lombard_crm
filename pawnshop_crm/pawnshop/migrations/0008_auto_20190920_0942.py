# Generated by Django 2.1.5 on 2019-09-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0007_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='category',
            field=models.ManyToManyField(related_name='criteries', to='pawnshop.Category', verbose_name='Относится к категории'),
        ),
    ]