# Generated by Django 3.0.7 on 2021-05-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0026_itemcart_multistaff_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='free_sessions',
            field=models.CharField(blank=True, db_column='Free_Sessions', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='treatment_no',
            field=models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True),
        ),
    ]