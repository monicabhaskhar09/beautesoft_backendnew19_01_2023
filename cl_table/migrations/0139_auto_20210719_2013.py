# Generated by Django 3.0.7 on 2021-07-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0138_auto_20210719_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cardno1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cardno2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cardno3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cardno4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cardno5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='emergencycontact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]