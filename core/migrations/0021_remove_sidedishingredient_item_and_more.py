# Generated by Django 4.0.4 on 2022-07-07 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_drinkingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidedishingredient',
            name='item',
        ),
        migrations.DeleteModel(
            name='MainCourseIngredient',
        ),
        migrations.DeleteModel(
            name='SideDishIngredient',
        ),
    ]
