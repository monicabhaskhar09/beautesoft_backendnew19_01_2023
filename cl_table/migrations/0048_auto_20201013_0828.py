# Generated by Django 3.0.7 on 2020-10-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0047_auto_20201013_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_class',
            field=models.CharField(blank=True, db_column='Item_Class', default=False, max_length=20, null=True),
        ),
    ]