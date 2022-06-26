# Generated by Django 4.0.5 on 2022-06-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_venue_venue_num_customerlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlocation',
            name='location',
            field=models.CharField(choices=[('Bar Vegan', 'Bar Vegan'), ('Sparrow', 'Sparrow')], max_length=100),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_num',
            field=models.CharField(blank=True, default='8470163253', editable=False, max_length=10, unique=True),
        ),
    ]