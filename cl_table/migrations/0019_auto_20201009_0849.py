# Generated by Django 3.0.7 on 2020-10-09 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0002_auto_20201009_0613'),
        ('custom', '0002_auto_20201009_0626'),
        ('cl_table', '0018_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='Appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Appointment'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='Trmt_Room_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.Room'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='add_duration',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='is_payment',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='isfoc',
            field=models.BooleanField(blank=True, db_column='isFOC', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='treatment_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.TreatmentAccount'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='lpackage',
            field=models.BooleanField(db_column='lPackage', null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='record_status',
            field=models.CharField(blank=True, choices=[('Pending', 'PENDING')], db_column='Record_Status', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='sa_status',
            field=models.CharField(blank=True, choices=[('SA', 'SA'), ('VT', 'VT'), ('SU', 'SU')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='site_code',
            field=models.CharField(blank=True, db_column='Site_Code', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Done', 'Done'), ('Cancel', 'Cancel')], db_column='Status', default='open', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_code',
            field=models.CharField(db_column='Treatment_Code', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_date',
            field=models.DateTimeField(auto_now_add=True, db_column='Treatment_Date', null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='trmt_is_auto_proportion',
            field=models.BooleanField(db_column='Trmt_Is_Auto_Proportion', null=True),
        ),
    ]