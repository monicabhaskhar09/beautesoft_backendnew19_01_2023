# Generated by Django 3.0.7 on 2022-11-29 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0007_webconsultation_analysisresult'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='webconsultation_analysisresult',
            unique_together={('doc_no',)},
        ),
    ]
