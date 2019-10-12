# Generated by Django 2.1.5 on 2019-10-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0022_auto_20191010_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledgeitem',
            name='loan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pledge_items', to='pawnshop.Loan', verbose_name='Займ'),
        ),
    ]