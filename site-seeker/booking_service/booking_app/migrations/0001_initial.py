# Generated by Django 5.0.7 on 2024-07-24 17:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('campsite_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_people', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ['check_in_date'],
            },
        ),
    ]
