# Generated by Django 2.2 on 2019-07-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0014_auto_20190720_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='notes',
        ),
        migrations.AddField(
            model_name='notes',
            name='content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
