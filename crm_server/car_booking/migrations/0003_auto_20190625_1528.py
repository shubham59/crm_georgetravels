# Generated by Django 2.2 on 2019-06-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking', '0002_auto_20190615_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbooking',
            name='num_days',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
