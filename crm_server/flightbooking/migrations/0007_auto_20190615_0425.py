# Generated by Django 2.2 on 2019-06-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0006_auto_20190614_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='adult_net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='adult_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='adult_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='gross',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_net',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_total',
            field=models.FloatField(default=0.0),
        ),
    ]
