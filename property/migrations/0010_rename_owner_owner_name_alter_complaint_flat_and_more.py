# Generated by Django 4.1.2 on 2022-10-20 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0009_rename_owners_phonenumber_owner_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='property.flat'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
