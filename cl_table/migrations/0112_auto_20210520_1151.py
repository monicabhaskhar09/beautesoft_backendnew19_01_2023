# Generated by Django 3.0.7 on 2021-05-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0111_auto_20210520_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmptreatment',
            name='lpackage',
            field=models.BooleanField(blank=True, db_column='lPackage', null=True),
        ),
    ]