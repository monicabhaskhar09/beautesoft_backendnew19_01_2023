# Generated by Django 3.0.7 on 2021-09-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0046_itemsitelist_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsitelist',
            name='is_dragappt',
            field=models.BooleanField(db_column='is_dragappt', default=False),
        ),
        migrations.AddField(
            model_name='itemsitelist',
            name='is_empvalidate',
            field=models.BooleanField(db_column='is_empvalidate', default=False),
        ),
    ]
