# Generated by Django 3.0.7 on 2022-02-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clpayroll', '0006_auto_20220215_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_salary',
            name='isactive',
            field=models.BooleanField(db_column='isactive', default=True),
        ),
    ]