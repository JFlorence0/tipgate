# Generated by Django 4.0.4 on 2022-07-01 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_customerorder_side_alter_customerorder_drink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]