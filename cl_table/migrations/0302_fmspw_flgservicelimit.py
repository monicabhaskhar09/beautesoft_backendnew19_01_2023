# Generated by Django 3.0.7 on 2022-11-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0301_itembatchsno'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmspw',
            name='flgservicelimit',
            field=models.BooleanField(db_column='flgservicelimit', default=False),
        ),
    ]
