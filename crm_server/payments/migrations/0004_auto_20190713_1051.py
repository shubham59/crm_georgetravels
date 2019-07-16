# Generated by Django 2.2 on 2019-07-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20190713_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='amount_due',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='payments',
            name='amount_paid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='payments',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='first_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='fourth_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='second_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='third_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
