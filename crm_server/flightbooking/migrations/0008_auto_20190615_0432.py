# Generated by Django 2.2 on 2019-06-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0007_auto_20190615_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='adult_gross',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='adult_gross_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='adult_gross_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_gross',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_gross_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='child_gross_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_gross',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_gross_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='infant_gross_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_gross',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_gross_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='youth_gross_total',
            field=models.FloatField(default=0.0),
        ),
    ]