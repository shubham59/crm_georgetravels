# Generated by Django 2.2 on 2019-06-27 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0014_flight_added_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airline',
            options={'ordering': ['-id']},
        ),
    ]
