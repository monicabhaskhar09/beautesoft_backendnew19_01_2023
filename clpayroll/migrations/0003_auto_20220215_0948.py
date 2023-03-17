# Generated by Django 3.0.7 on 2022-02-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clpayroll', '0002_auto_20220215_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_salary',
            name='emp_name',
            field=models.CharField(blank=True, db_column='Emp_name', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='employee_salary',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee_salary',
            name='is_active',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('In Active', 'In Active'), ('All', 'All')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employee_salary',
            name='salarystatus',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Open', 'Open'), ('Posted', 'Posted')], default='New', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employee_salary',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]