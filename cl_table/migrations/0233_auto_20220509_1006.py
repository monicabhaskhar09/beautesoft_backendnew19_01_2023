# Generated by Django 3.0.7 on 2022-05-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0232_treatment_is_datainsert'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='bookedby',
            field=models.CharField(blank=True, db_column='bookedby', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='editedby',
            field=models.CharField(blank=True, db_column='editedby', max_length=200, null=True),
        ),
    ]
