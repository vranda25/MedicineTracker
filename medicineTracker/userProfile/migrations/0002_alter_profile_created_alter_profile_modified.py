# Generated by Django 4.1.7 on 2023-03-27 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 27, 5, 47, 34, 763074, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 27, 5, 47, 34, 763074, tzinfo=datetime.timezone.utc)),
        ),
    ]
