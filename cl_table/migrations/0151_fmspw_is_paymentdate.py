# Generated by Django 3.0.7 on 2021-08-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0150_auto_20210804_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmspw',
            name='is_paymentdate',
            field=models.BooleanField(db_column='PaymentDate', default=False),
        ),
    ]