# Generated by Django 3.0.7 on 2023-09-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0130_auto_20230731_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='prepaid_deposit',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]