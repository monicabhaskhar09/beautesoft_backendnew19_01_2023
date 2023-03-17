# Generated by Django 3.0.7 on 2022-05-09 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0084_delete_poitemmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='POItemModel',
            fields=[
                ('id', models.AutoField(db_column='PO_Item_ID', primary_key=True, serialize=False)),
                ('po_quantity', models.CharField(blank=True, db_column='PO_Item_Quantity', default='', max_length=255, null=True)),
                ('po_unitprice', models.CharField(blank=True, db_column='PO_Item_UnitPrice', default='', max_length=255, null=True)),
                ('po_itemremarks', models.CharField(blank=True, db_column='PO_Item_Remarks', default='', max_length=255, null=True)),
                ('po_itemcode', models.CharField(blank=True, db_column='PO_Item_Code', default='', max_length=255, null=True)),
                ('po_itemdesc', models.CharField(blank=True, db_column='PO_Item_Desc', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('fk_po', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.POModel')),
            ],
            options={
                'db_table': 'PurchaseOrder_Item',
            },
        ),
    ]