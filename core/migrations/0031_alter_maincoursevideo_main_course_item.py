# Generated by Django 4.0.4 on 2022-07-08 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_maincoursevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincoursevideo',
            name='main_course_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.maincourse'),
        ),
    ]
