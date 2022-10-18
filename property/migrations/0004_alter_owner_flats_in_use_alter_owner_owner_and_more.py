# Generated by Django 4.1.2 on 2022-10-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20221018_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats_in_use',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='flat_use', to='property.flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]