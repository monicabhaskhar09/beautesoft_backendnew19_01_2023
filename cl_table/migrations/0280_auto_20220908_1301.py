# Generated by Django 3.0.7 on 2022-09-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0279_auto_20220908_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytable',
            name='pay_is_rounding',
            field=models.BooleanField(blank=True, db_column='Pay_Is_Rounding', default=False, null=True),
        ),
    ]
