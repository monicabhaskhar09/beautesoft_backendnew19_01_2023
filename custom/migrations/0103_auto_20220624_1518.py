# Generated by Django 3.0.7 on 2022-06-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0102_quotationpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencytable',
            name='curr_isactive',
            field=models.BooleanField(blank=True, db_column='Curr_isactive', default=False, null=True),
        ),
        migrations.AlterField(
            model_name='currencytable',
            name='curr_name',
            field=models.CharField(blank=True, db_column='Curr_Name', max_length=255, null=True),
        ),
    ]
