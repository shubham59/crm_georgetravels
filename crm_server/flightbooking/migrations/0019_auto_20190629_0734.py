# Generated by Django 2.2 on 2019-06-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0018_passenger_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='airline_ref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='pnr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
