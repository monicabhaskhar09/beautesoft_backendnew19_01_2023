# Generated by Django 3.0.7 on 2020-10-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0042_auto_20201011_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='equipmentcost',
        ),
    ]