# Generated by Django 3.0.7 on 2021-05-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0103_auto_20210421_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemhelper',
            name='percent',
            field=models.FloatField(blank=True, db_column='Percent', null=True),
        ),
        migrations.AddField(
            model_name='itemhelper',
            name='work_amt',
            field=models.FloatField(blank=True, db_column='Work_Amount', null=True),
        ),
        migrations.AddField(
            model_name='tmpitemhelper',
            name='percent',
            field=models.FloatField(blank=True, db_column='Percent', null=True),
        ),
        migrations.AddField(
            model_name='tmpitemhelper',
            name='work_amt',
            field=models.FloatField(blank=True, db_column='Work_Amount', null=True),
        ),
    ]