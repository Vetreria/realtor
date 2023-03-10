# Generated by Django 4.1.5 on 2023-01-03 10:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0013_auto_20230103_1020"),
    ]

    operations = [
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="ФИО владельца"),
                ),
                (
                    "owners_phonenumber",
                    models.CharField(
                        max_length=20, null=True, verbose_name="Номер владельца"
                    ),
                ),
                (
                    "owner_pure_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        region=None,
                        verbose_name="Нормализованный номер владельца",
                    ),
                ),
                (
                    "owned_flats",
                    models.ManyToManyField(
                        blank=True,
                        related_name="flat_owners",
                        to="property.flat",
                        verbose_name="Квартиры в собственности",
                    ),
                ),
            ],
        ),
    ]
