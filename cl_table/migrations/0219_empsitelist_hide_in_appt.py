# Generated by Django 3.0.7 on 2022-04-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0218_customerdocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='empsitelist',
            name='hide_in_appt',
            field=models.BooleanField(db_column='hide_in_appt', null=True),
        ),
    ]
