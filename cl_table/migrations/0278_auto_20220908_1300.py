# Generated by Django 3.0.7 on 2022-09-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0277_paytable_pay_is_rounding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytable',
            name='pay_is_rounding',
            field=models.BooleanField(blank=True, db_column='Pay_Is_Rounding', default=False, null=True),
        ),
    ]