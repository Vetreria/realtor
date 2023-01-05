# Generated by Django 2.2.24 on 2023-01-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20230105_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owned_flats',
        ),
        migrations.AddField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
