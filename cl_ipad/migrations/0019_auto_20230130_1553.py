# Generated by Django 3.0.7 on 2023-01-30 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0018_auto_20230102_1701'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TNC_Detail',
        ),
        migrations.DeleteModel(
            name='TNC_Header',
        ),
    ]