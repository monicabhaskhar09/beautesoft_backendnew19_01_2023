# Generated by Django 3.0.7 on 2022-06-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0242_custlogaudit'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='isdelete',
            field=models.BooleanField(db_column='IsDelete', null=True),
        ),
    ]