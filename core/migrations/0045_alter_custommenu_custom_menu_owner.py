# Generated by Django 4.0.5 on 2022-07-19 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_customerlocation_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custommenu',
            name='custom_menu_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venue'),
        ),
    ]
