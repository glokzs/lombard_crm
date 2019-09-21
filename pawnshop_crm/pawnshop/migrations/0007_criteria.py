# Generated by Django 2.1.5 on 2019-09-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0006_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, verbose_name='Название критерия')),
                ('category', models.ManyToManyField(default=None, related_name='criteries', to='pawnshop.Category', verbose_name='Относится к категории')),
            ],
            options={
                'verbose_name': 'Критерий',
                'verbose_name_plural': 'Критерии',
            },
        ),
    ]