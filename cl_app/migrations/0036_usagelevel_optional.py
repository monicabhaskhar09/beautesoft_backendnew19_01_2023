# Generated by Django 3.0.7 on 2021-04-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0035_auto_20210430_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='usagelevel',
            name='optional',
            field=models.BooleanField(db_column='Optional', default=False),
            preserve_default=False,
        ),
    ]
