# Generated by Django 3.0.7 on 2023-01-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0317_item_membershipprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerclass',
            name='package_code',
            field=models.CharField(blank=True, db_column='Package_Code', max_length=50, null=True),
        ),
    ]
