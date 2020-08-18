# Generated by Django 3.0.3 on 2020-08-17 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200804_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='update_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='estimated_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]