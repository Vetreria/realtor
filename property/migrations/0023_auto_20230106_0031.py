# Generated by Django 2.2.24 on 2023-01-05 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20230106_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim_flat', to='property.Flat', verbose_name='Претензия по квартире:'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owner_flats', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
