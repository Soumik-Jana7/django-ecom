# Generated by Django 4.1.7 on 2023-03-05 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auctionproduct_status_alter_auctionproduct_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 12, 23, 31, 335878)),
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 12, 23, 31, 335878)),
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='status',
            field=models.BooleanField(default='False'),
        ),
    ]
