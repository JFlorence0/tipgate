# Generated by Django 4.0.4 on 2022-07-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_maincoursevideo_main_course_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_menu_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.venue')),
            ],
        ),
    ]
