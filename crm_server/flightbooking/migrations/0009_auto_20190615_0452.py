# Generated by Django 2.2 on 2019-06-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0008_auto_20190615_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='baggage_allowance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='e_ticket',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='issue_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='supplier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
