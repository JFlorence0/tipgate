# Generated by Django 4.0.5 on 2022-06-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customerlocation_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='venue_num',
            field=models.CharField(blank=True, default='7179354583', editable=False, max_length=10, unique=True),
        ),
    ]
