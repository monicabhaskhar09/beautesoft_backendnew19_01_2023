# Generated by Django 3.0.7 on 2021-08-23 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0152_auto_20210819_1547'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='poshaud',
            unique_together={('cas_logno', 'sa_transacno', 'sa_custno', 'itemsite_code', 'sa_transacno_ref')},
        ),
    ]