# Generated by Django 2.2 on 2019-07-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payments_added_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='expiry_date',
            new_name='expiry_month',
        ),
        migrations.AddField(
            model_name='payments',
            name='expiry_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
