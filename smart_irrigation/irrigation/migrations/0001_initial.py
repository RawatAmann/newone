# Generated by Django 5.2 on 2025-04-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('soil_moisture', models.FloatField()),
                ('weather', models.CharField(max_length=100)),
                ('irrigation_zone', models.CharField(max_length=100)),
            ],
        ),
    ]
