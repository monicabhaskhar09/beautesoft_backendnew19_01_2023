# Generated by Django 3.0.7 on 2022-02-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0200_packageauditinglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='packageauditinglog',
            name='pa_qty',
            field=models.IntegerField(blank=True, db_column='pa_qty', null=True),
        ),
    ]