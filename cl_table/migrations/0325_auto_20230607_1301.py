# Generated by Django 3.0.7 on 2023-06-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0324_auto_20230607_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidaccountcondition',
            name='pp_desc',
            field=models.CharField(blank=True, db_column='PP_DESC', max_length=250, null=True),
        ),
    ]
