# Generated by Django 3.0.7 on 2020-10-16 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0062_auto_20201016_0855'),
        ('custom', '0004_auto_20201009_1838'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemCart',
        ),
    ]