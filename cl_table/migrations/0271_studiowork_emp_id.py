# Generated by Django 3.0.7 on 2022-09-02 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0270_appointment_dt_lineno'),
    ]

    operations = [
        migrations.AddField(
            model_name='studiowork',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee'),
        ),
    ]
