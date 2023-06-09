# Generated by Django 3.0.7 on 2022-10-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0054_itemsitelist_is_exclusive'),
        ('cl_table', '0287_auto_20221005_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgmpolicycloud',
            name='site_ids',
            field=models.ManyToManyField(blank=True, to='cl_app.ItemSitelist'),
        ),
        migrations.AlterUniqueTogether(
            name='mgmpolicycloud',
            unique_together={('level', 'point_value')},
        ),
        migrations.RemoveField(
            model_name='mgmpolicycloud',
            name='Site_Codeid',
        ),
        migrations.RemoveField(
            model_name='mgmpolicycloud',
            name='site_code',
        ),
    ]
