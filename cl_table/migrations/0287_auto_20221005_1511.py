# Generated by Django 3.0.7 on 2022-10-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0286_auto_20220929_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stktrn',
            name='trn_date',
            field=models.DateTimeField(db_column='TRN_DATE', null=True),
        ),
        migrations.AlterField(
            model_name='stktrn',
            name='trn_post',
            field=models.DateTimeField(db_column='TRN_POST', null=True),
        ),
    ]
