# Generated by Django 4.0.5 on 2022-06-25 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_venue_venue_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venue')),
            ],
        ),
    ]
