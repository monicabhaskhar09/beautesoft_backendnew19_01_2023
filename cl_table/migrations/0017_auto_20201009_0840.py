# Generated by Django 3.0.7 on 2020-10-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0002_auto_20201009_0613'),
        ('cl_table', '0016_postaud'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaud',
            name='Appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Appointment'),
        ),
        migrations.AddField(
            model_name='postaud',
            name='ItemSIte_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='postaud',
            name='billable_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='credit_debit',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='discount_amt',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='is_voucher',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='pay_premise',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='points',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='posdaudlineamountassign',
            field=models.CharField(blank=True, db_column='posdaudLineAmountAssign', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='posdaudlineamountused',
            field=models.FloatField(blank=True, db_column='posdaudLineAmountUsed', null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='posdaudlineno',
            field=models.CharField(blank=True, db_column='POSDAUDLineNo', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='pp_bal',
            field=models.FloatField(blank=True, db_column='PP_Bal', null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='prepaid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='subtotal',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='tax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='voucher_amt',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='postaud',
            name='voucher_no',
            field=models.CharField(db_column='Voucher_No', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='cas_logno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='dt_lineno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='itemsite_code',
            field=models.CharField(db_column='ItemSIte_Code', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='pay_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='sa_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='sa_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='postaud',
            name='sa_transacno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]