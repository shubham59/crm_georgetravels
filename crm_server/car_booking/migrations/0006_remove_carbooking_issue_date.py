# Generated by Django 2.2 on 2019-07-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking', '0005_carbooking_issue_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbooking',
            name='issue_date',
        ),
    ]
