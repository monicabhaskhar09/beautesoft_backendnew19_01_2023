# Generated by Django 3.0.7 on 2021-07-19 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0136_auto_20210719_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Cust_titleid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.CustomerTitle'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_consultant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_consultant', to='cl_table.Employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_therapist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_therapist', to='cl_table.Employee'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='cust_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer'),
        ),
        migrations.AddField(
            model_name='schedulehour',
            name='shortdesc',
            field=models.CharField(db_column='shortDesc', max_length=2, null=True),
        ),
    ]
