# Generated by Django 3.0.7 on 2021-07-19 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0130_auto_20210719_1542'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='diagnosis',
            unique_together={('sys_code', 'cust_no', 'site_code')},
        ),
    ]