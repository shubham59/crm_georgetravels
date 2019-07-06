# Generated by Django 2.2 on 2019-07-04 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_history_added_timestamp'),
        ('cruisebooking', '0002_remove_cruisehire_issue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruisehire',
            name='booking_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookings.Booking'),
            preserve_default=False,
        ),
    ]
