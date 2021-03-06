# Generated by Django 2.1.7 on 2019-02-17 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=100)),
                ('is_active', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
