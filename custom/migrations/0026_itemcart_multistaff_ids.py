# Generated by Django 3.0.7 on 2021-05-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0106_auto_20210512_1053'),
        ('custom', '0025_auto_20210505_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='multistaff_ids',
            field=models.ManyToManyField(blank=True, related_name='multistaff', to='cl_table.Tmpmultistaff'),
        ),
    ]