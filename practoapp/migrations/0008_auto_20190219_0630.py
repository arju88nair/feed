# Generated by Django 2.1.7 on 2019-02-19 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practoapp', '0007_auto_20190219_0630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='doctor_id',
            new_name='doctor_availability',
        ),
    ]
