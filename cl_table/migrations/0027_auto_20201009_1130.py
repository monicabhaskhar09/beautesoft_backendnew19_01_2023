# Generated by Django 3.0.7 on 2020-10-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0026_attendance2_controlno_empsitelist_itemclass_itemdept_itemdiv_itemhelper_itemrange_multistaff_paygrou'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemclass',
            name='process_remark',
            field=models.CharField(blank=True, db_column='Process_Remark', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='itemdept',
            name='process_remark',
            field=models.CharField(blank=True, db_column='Process_Remark', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='itemdiv',
            name='process_remark',
            field=models.CharField(blank=True, db_column='Process_Remark', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='itemrange',
            name='process_remark',
            field=models.CharField(blank=True, db_column='Process_Remark', max_length=250, null=True),
        ),
    ]
