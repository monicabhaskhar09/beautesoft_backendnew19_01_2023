# Generated by Django 3.0.7 on 2023-06-01 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0129_auto_20230601_1345'),
        ('cl_table', '0321_auto_20230329_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepaidaccount',
            name='terminate_prepaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prepaidaccountcondition',
            name='itembrand_id',
            field=models.IntegerField(blank=True, db_column='itembrand_id', null=True),
        ),
        migrations.AddField(
            model_name='prepaidaccountcondition',
            name='itemdept_id',
            field=models.IntegerField(blank=True, db_column='itemdept_id', null=True),
        ),
        migrations.AddField(
            model_name='prepaidopencondition',
            name='itembrand_id',
            field=models.IntegerField(blank=True, db_column='itembrand_id', null=True),
        ),
        migrations.AddField(
            model_name='prepaidopencondition',
            name='itemcart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ItemCart'),
        ),
        migrations.AddField(
            model_name='prepaidopencondition',
            name='itemdept_id',
            field=models.IntegerField(blank=True, db_column='itemdept_id', null=True),
        ),
        migrations.AddField(
            model_name='vouchercondition',
            name='isactive',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AddField(
            model_name='vouchercondition',
            name='line_no',
            field=models.IntegerField(blank=True, db_column='Line_No', null=True),
        ),
        migrations.AlterField(
            model_name='prepaidaccountcondition',
            name='conditiontype1',
            field=models.CharField(db_column='ConditionType1', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='prepaidaccountcondition',
            name='conditiontype2',
            field=models.CharField(db_column='ConditionType2', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='prepaidopencondition',
            name='conditiontype1',
            field=models.CharField(db_column='ConditionType1', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='prepaidopencondition',
            name='conditiontype2',
            field=models.CharField(db_column='ConditionType2', max_length=80, null=True),
        ),
    ]