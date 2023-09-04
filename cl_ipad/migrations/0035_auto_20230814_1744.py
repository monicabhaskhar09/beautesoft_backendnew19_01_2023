# Generated by Django 3.0.7 on 2023-08-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0034_webconsultation_analysismaster_is_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='webconsultation_analysisresult',
            name='image',
            field=models.ImageField(blank=True, db_column='image', max_length=255, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='webconsultation_analysisresult',
            name='pic_data1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='webconsultation_analysismaster',
            unique_together=set(),
        ),
    ]
