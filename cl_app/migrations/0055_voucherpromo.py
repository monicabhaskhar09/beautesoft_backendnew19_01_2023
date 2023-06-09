# Generated by Django 3.0.7 on 2022-11-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0054_itemsitelist_is_exclusive'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherPromo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('voucher_code', models.CharField(blank=True, db_column='voucher_code', max_length=200, null=True)),
                ('voucher_desc', models.CharField(blank=True, db_column='voucher_desc', max_length=500, null=True)),
                ('sms_text', models.TextField(blank=True, db_column='sms_text', null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'VoucherPromo',
            },
        ),
    ]
