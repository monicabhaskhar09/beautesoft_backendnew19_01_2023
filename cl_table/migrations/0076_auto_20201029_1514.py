# Generated by Django 3.0.7 on 2020-10-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0075_auto_20201029_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositaccount',
            name='sa_staffno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]