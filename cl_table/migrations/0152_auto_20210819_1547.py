# Generated by Django 3.0.7 on 2021-08-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0151_fmspw_is_paymentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.BooleanField(blank=True, db_column='balance', default=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.BooleanField(blank=True, db_column='birthday', default=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='outstanding',
            field=models.BooleanField(blank=True, db_column='outstanding', default=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='outstanding_amt',
            field=models.FloatField(null=True),
        ),
    ]
