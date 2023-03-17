# Generated by Django 3.0.7 on 2020-10-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0032_auto_20201009_1531'),
        ('cl_app', '0002_auto_20201009_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsitelist',
            name='ItemSite_Cityid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.City'),
        ),
        migrations.AddField(
            model_name='itemsitelist',
            name='ItemSite_Countryid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Country'),
        ),
        migrations.AddField(
            model_name='itemsitelist',
            name='ItemSite_Stateid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.State'),
        ),
        migrations.AddField(
            model_name='itemsitelist',
            name='ItemSite_Userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Fmspw'),
        ),
        migrations.AddField(
            model_name='itemsitelist',
            name='services',
            field=models.ManyToManyField(blank=True, to='cl_table.Stock'),
        ),
    ]