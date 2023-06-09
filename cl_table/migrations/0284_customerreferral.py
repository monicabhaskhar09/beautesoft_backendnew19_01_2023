# Generated by Django 3.0.7 on 2022-09-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0054_itemsitelist_is_exclusive'),
        ('cl_table', '0283_mgmpolicycloud_point_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReferral',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('site_code', models.CharField(db_column='Site_Code', max_length=20, null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cust_totpurchasevalue', models.FloatField(blank=True, null=True)),
                ('Site_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='custid', to='cl_table.Customer')),
                ('referral_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='referralid', to='cl_table.Customer')),
            ],
            options={
                'db_table': 'CustomerReferral',
                'unique_together': {('referral_id', 'cust_id', 'Site_Codeid')},
            },
        ),
    ]
