# Generated by Django 3.0.7 on 2021-09-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0047_auto_20210901_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsitelist',
            name='is_dragappt',
            field=models.BooleanField(db_column='is_dragappt', default=True),
        ),
        migrations.AlterField(
            model_name='itemsitelist',
            name='is_empvalidate',
            field=models.BooleanField(db_column='is_empvalidate', default=True),
        ),
    ]