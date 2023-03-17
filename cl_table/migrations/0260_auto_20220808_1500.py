# Generated by Django 3.0.7 on 2022-08-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0052_auto_20220713_1928'),
        ('cl_table', '0259_auto_20220728_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatmentpackage',
            old_name='packagetype',
            new_name='type',
        ),
        migrations.AddField(
            model_name='treatmentpackage',
            name='Item_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock'),
        ),
        migrations.AddField(
            model_name='treatmentpackage',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='treatmentpackage',
            name='site_code',
            field=models.CharField(blank=True, db_column='Site_Code', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='treatmentpackage',
            name='treatment_date',
            field=models.DateTimeField(auto_now_add=True, db_column='Treatment_Date', null=True),
        ),
        migrations.AddField(
            model_name='treatmentpackage',
            name='treatment_limit_times',
            field=models.FloatField(blank=True, db_column='Treatment_Limit_Times', null=True),
        ),
    ]