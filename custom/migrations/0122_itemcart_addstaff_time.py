# Generated by Django 3.0.7 on 2022-11-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0121_auto_20221011_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='addstaff_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
