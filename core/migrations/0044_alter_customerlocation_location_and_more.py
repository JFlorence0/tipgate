# Generated by Django 4.0.5 on 2022-07-18 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_alter_selectcustommenu_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlocation',
            name='location',
            field=models.CharField(choices=[('Bar Vegan', 'Bar Vegan'), ('Sparrow', 'Sparrow'), ('Slutty Vegan', 'Slutty Vegan'), ('Restaurant', 'Restaurant'), ('Starbucks', 'Starbucks'), ('Starbucks', 'Starbucks')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='venue',
            field=models.CharField(choices=[('Bar Vegan', 'Bar Vegan'), ('Sparrow', 'Sparrow'), ('Slutty Vegan', 'Slutty Vegan'), ('Restaurant', 'Restaurant'), ('Starbucks', 'Starbucks'), ('Starbucks', 'Starbucks')], max_length=100),
        ),
        migrations.AlterField(
            model_name='selectcustommenu',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venue'),
        ),
        migrations.AlterField(
            model_name='serverlocation',
            name='location',
            field=models.CharField(choices=[('Bar Vegan', 'Bar Vegan'), ('Sparrow', 'Sparrow'), ('Slutty Vegan', 'Slutty Vegan'), ('Restaurant', 'Restaurant'), ('Starbucks', 'Starbucks'), ('Starbucks', 'Starbucks')], max_length=100),
        ),
    ]
