# Generated by Django 2.1.5 on 2019-10-10 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0021_merge_20191003_0431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='pledge_item',
        ),
        migrations.AddField(
            model_name='pledgeitem',
            name='loan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pledge_items', to='pawnshop.Loan', verbose_name='Займ'),
        ),
    ]