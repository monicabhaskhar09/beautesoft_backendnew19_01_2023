# Generated by Django 3.0.7 on 2021-12-21 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0057_commdeduction_commissionprofile_commtarget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commdeduction',
            name='employe_level',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='brand_comm',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='department_comm',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='employe_level',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='item',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='rangee',
        ),
        migrations.RemoveField(
            model_name='commissionprofile',
            name='rangee_comm',
        ),
        migrations.RemoveField(
            model_name='commtarget',
            name='employe_level',
        ),
        migrations.AddField(
            model_name='commdeduction',
            name='comm_Profilede_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.CommissionProfile'),
        ),
        migrations.AddField(
            model_name='commdeduction',
            name='employe_level_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom.EmpLevel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='brand_comm_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='range_brand', to='custom.ItemBrandModel'),
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='brand_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom.ItemBrandModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='department_comm_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='range_dept', to='custom.ItemDeptModel'),
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='department_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item_department', to='custom.ItemDeptModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='employe_level_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.EmpLevel'),
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='range_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom.ItemRangeModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commissionprofile',
            name='rangee_comm_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='range_commission', to='custom.ItemRangeModel'),
        ),
        migrations.AddField(
            model_name='commtarget',
            name='comm_Profile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.CommissionProfile'),
        ),
        migrations.AddField(
            model_name='commtarget',
            name='employe_level_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom.EmpLevel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='bank_changes',
            field=models.FloatField(blank=True, db_column='Bank changes', null=True),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='bc_ispercent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='emi',
            field=models.FloatField(blank=True, db_column='EMI', null=True),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='emi_ispercent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='gst',
            field=models.FloatField(blank=True, db_column='GST', null=True),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='gst_ispercent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commdeduction',
            name='profile_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='commissionprofile',
            name='commission_type',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='commissionprofile',
            name='profile_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='commtarget',
            name='incentive_ispercent_comm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commtarget',
            name='ispercent_comm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commtarget',
            name='max_value_comm',
            field=models.FloatField(blank=True, db_column='Target max comm', null=True),
        ),
        migrations.AlterField(
            model_name='commtarget',
            name='min_value_comm',
            field=models.FloatField(blank=True, db_column='Target min comm', null=True),
        ),
        migrations.AlterField(
            model_name='commtarget',
            name='profile_name',
            field=models.CharField(max_length=255),
        ),
    ]