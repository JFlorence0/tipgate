# Generated by Django 4.0.4 on 2022-07-07 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_maincourse_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincourse',
            name='video',
        ),
    ]
