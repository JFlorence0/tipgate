# Generated by Django 4.0.4 on 2022-07-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_maincourse_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincourse',
            name='ingredient1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
