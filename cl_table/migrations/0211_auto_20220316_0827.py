# Generated by Django 3.0.7 on 2022-03-16 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0210_auto_20220316_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redeempolicy',
            old_name='itemdiv_ids',
            new_name='item_divids',
        ),
    ]
