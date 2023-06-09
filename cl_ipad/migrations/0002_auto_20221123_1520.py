# Generated by Django 3.0.7 on 2022-11-23 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0306_auto_20221118_1309'),
        ('cl_ipad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webconsultation_hdr',
            name='cust_codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer'),
        ),
        migrations.AddField(
            model_name='webconsultation_hdr',
            name='emp_codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee'),
        ),
        migrations.AddField(
            model_name='webconsultation_hdr',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
