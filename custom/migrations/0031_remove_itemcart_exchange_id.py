# Generated by Django 3.0.7 on 2021-05-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0030_itemcart_exchange_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcart',
            name='exchange_id',
        ),
    ]