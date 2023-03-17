# Generated by Django 3.0.7 on 2020-11-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0085_auto_20201116_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidaccount',
            name='sa_status',
            field=models.CharField(blank=True, choices=[('DEPOSIT', 'DEPOSIT'), ('TOPUP', 'TOPUP'), ('SA', 'SA'), ('VT', 'VT')], db_column='SA_STATUS', max_length=50, null=True),
        ),
    ]