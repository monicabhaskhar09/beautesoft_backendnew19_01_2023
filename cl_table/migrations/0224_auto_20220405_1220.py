# Generated by Django 3.0.7 on 2022-04-05 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0223_apptchannel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Appt_typeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.ApptChannel'),
        ),
    ]