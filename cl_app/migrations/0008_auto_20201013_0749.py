# Generated by Django 3.0.7 on 2020-10-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0007_auto_20201013_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsitelist',
            name='systemlog_mdpl_update',
            field=models.BooleanField(db_column='SystemLog_MDPL_Update', default=False, null=True),
        ),
    ]