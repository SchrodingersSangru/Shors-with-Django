# Generated by Django 2.0.12 on 2022-08-12 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shors', '0003_auto_20220812_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
