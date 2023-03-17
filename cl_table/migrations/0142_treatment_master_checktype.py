# Generated by Django 3.0.7 on 2021-07-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0141_remove_treatment_master_checktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment_master',
            name='checktype',
            field=models.CharField(blank=True, choices=[('service', 'service'), ('package', 'package'), ('freetext', 'freetext')], db_column='Check_Type', max_length=50, null=True),
        ),
    ]
