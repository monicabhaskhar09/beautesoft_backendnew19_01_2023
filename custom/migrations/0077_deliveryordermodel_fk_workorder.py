# Generated by Django 3.0.7 on 2022-05-04 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0076_deliveryorderaddrmodel_deliveryorderdetailmodel_deliveryorderitemmodel_deliveryordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryordermodel',
            name='fk_workorder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.WorkOrderInvoiceModel'),
        ),
    ]
