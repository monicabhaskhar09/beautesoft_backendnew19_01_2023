# Generated by Django 3.0.7 on 2021-12-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0186_itembatch_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytable',
            name='pay_color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
