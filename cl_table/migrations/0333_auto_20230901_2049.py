# Generated by Django 3.0.7 on 2023-09-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0332_auto_20230901_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemhelper',
            name='sa_date',
            field=models.DateTimeField(null=True),
        ),
    ]
