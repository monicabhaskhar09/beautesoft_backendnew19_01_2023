# Generated by Django 3.0.7 on 2022-12-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0124_auto_20221208_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smtpsettings',
            name='user_password',
            field=models.CharField(blank=True, db_column='User_Password', max_length=2000, null=True),
        ),
    ]
