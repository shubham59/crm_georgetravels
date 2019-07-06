# Generated by Django 2.2 on 2019-06-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0012_auto_20190625_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='airline_class',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='airline_name',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='airline_number',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='arr_airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='arr_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='dep_airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='dep_date',
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(blank=True, max_length=100, null=True)),
                ('airline_number', models.CharField(blank=True, max_length=100, null=True)),
                ('dep_airport', models.CharField(blank=True, max_length=100, null=True)),
                ('dep_date', models.DateTimeField(blank=True, null=True)),
                ('arr_airport', models.CharField(blank=True, max_length=100, null=True)),
                ('arr_date', models.DateTimeField(blank=True, null=True)),
                ('airline_class', models.CharField(blank=True, max_length=10, null=True)),
                ('Flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightbooking.Flight')),
            ],
        ),
    ]