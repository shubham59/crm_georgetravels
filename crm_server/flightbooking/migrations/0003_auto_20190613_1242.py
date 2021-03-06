# Generated by Django 2.2 on 2019-06-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0002_remove_passenger_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='airline',
            new_name='airline_name',
        ),
        migrations.AddField(
            model_name='flight',
            name='airline_class',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='airline_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arr_airport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arr_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='dep_airport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='dep_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
