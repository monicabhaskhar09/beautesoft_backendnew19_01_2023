# Generated by Django 3.0.7 on 2023-07-31 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0129_auto_20230601_1345'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]