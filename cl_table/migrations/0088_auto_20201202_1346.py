# Generated by Django 3.0.7 on 2020-12-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0087_remove_stock_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posdaud',
            name='record_detail_type',
            field=models.CharField(blank=True, choices=[('SERVICE', 'SERVICE'), ('TD', 'TD'), ('PRODUCT', 'PRODUCT'), ('PREPAID', 'PREPAID'), ('VOUCHER', 'VOUCHER'), ('PACKAGE', 'PACKAGE'), ('TP SERVICE', 'TP SERVICE'), ('TP PRODUCT', 'TP PRODUCT'), ('TP PREPAID', 'TP PREPAID')], db_column='Record_Detail_Type', max_length=50, null=True),
        ),
    ]