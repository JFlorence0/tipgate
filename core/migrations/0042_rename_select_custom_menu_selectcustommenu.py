# Generated by Django 4.0.5 on 2022-07-15 05:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0041_select_custom_menu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='select_custom_menu',
            new_name='SelectCustomMenu',
        ),
    ]
