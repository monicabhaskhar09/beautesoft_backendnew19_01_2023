# Generated by Django 3.0.7 on 2023-02-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0024_auto_20230216_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='webconsultation_question',
            name='mandatory',
            field=models.BooleanField(db_column='Mandatory', default=False),
        ),
    ]