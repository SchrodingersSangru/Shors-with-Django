# Generated by Django 2.0.12 on 2022-08-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]