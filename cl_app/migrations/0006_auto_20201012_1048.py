# Generated by Django 3.0.7 on 2020-10-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0005_auto_20201012_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitegroup',
            name='code',
            field=models.CharField(db_column='Code', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sitegroup',
            name='description',
            field=models.CharField(db_column='Description', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitegroup',
            name='is_delete',
            field=models.BooleanField(db_column='Is_Delete', null=True),
        ),
    ]