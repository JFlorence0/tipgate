# Generated by Django 4.0.5 on 2022-06-27 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_sidedishingredient_drinkingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkingredient',
            name='note_about_ingredient',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='maincourseingredient',
            name='note_about_ingredient',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sidedishingredient',
            name='note_about_ingredient',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]