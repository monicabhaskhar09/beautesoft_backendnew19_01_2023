# Generated by Django 3.0.7 on 2022-08-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0266_customerdocument_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='treatment_code',
            field=models.CharField(db_column='Treatment_Code', max_length=200, null=True),
        ),
    ]
