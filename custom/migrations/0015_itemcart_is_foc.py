# Generated by Django 3.0.7 on 2020-11-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0014_auto_20201106_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='is_foc',
            field=models.BooleanField(default=False),
        ),
    ]