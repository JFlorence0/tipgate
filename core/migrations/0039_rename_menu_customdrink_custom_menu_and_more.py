# Generated by Django 4.0.5 on 2022-07-14 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_alter_customerlocation_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customdrink',
            old_name='menu',
            new_name='custom_menu',
        ),
        migrations.RenameField(
            model_name='customsidedish',
            old_name='menu',
            new_name='custom_menu',
        ),
    ]