# Generated by Django 3.0.7 on 2022-11-24 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0057_smsprocesslog'),
        ('cl_ipad', '0005_auto_20221124_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='webconsultation_hdr',
            name='site_codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
    ]
