# Generated by Django 3.0.7 on 2023-09-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0326_auto_20230707_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxType2TaxCode',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('item_code', models.CharField(blank=True, db_column='ITEM_CODE', max_length=50, null=True)),
                ('tax_code', models.CharField(blank=True, db_column='TAX_CODE', max_length=20, null=True)),
                ('tax_desc', models.CharField(blank=True, db_column='TAX_DESC', max_length=1000, null=True)),
                ('tax_rate_percent', models.FloatField(blank=True, db_column='TAX_RATE_PERCENT', null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='ISACTIVE', null=True)),
                ('item_seq', models.FloatField(blank=True, db_column='ITEM_SEQ', null=True)),
            ],
            options={
                'db_table': 'TAX_TYPE2_TAX_CODE',
            },
        ),
    ]
