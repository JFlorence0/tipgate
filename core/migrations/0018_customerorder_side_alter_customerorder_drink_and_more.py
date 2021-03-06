# Generated by Django 4.0.4 on 2022-07-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_customerorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='side',
            field=models.CharField(choices=[('Steak Fries', 'Steak Fries')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='drink',
            field=models.CharField(choices=[('Still Water', 'Still Water')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='entree',
            field=models.CharField(choices=[('Beyond Burger', 'Beyond Burger'), ("Chik'n Sandwich", "Chik'n Sandwich")], max_length=100, null=True),
        ),
    ]
