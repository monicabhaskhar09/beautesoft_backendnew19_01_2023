# Generated by Django 3.0.7 on 2021-05-12 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0106_auto_20210512_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmpmultistaff',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee'),
        ),
    ]