# Generated by Django 3.0.7 on 2022-11-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0008_auto_20221129_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebConsultation_Referral',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cust_code', models.CharField(db_column='CustCode', max_length=255)),
                ('doc_no', models.CharField(blank=True, db_column='DocNo', max_length=255, null=True)),
                ('site_code', models.CharField(blank=True, db_column='SiteCode', max_length=20, null=True)),
                ('referral_name', models.CharField(db_column='ReferralName', max_length=255)),
                ('referral_age', models.IntegerField(db_column='ReferralAge')),
                ('referral_contactno', models.CharField(db_column='ReferralContactNo', max_length=255)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('create_date', models.DateTimeField(blank=True, db_column='CreateDate', null=True)),
                ('create_by', models.CharField(blank=True, db_column='CreateBy', max_length=20, null=True)),
                ('last_updatedate', models.DateTimeField(blank=True, db_column='LastUpdateDate', null=True)),
                ('last_updateby', models.CharField(blank=True, db_column='LastUpdateBy', max_length=20, null=True)),
                ('referral_code', models.CharField(blank=True, db_column='ReferralCode', max_length=255, null=True)),
            ],
            options={
                'db_table': 'WebConsultation_Referral',
            },
        ),
    ]
