# Generated by Django 3.0.7 on 2020-10-12 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0006_auto_20201012_1048'),
        ('cl_table', '0044_stock_equipmentcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
    ]