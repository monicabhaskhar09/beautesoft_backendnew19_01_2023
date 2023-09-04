# Generated by Django 3.0.7 on 2023-08-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0030_webconsultation_question_declaration_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebConsultation_AnalysisMaster',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('field_name', models.CharField(blank=True, db_column='fieldName', max_length=100, null=True)),
                ('display_field_name', models.CharField(blank=True, db_column='displayFieldName', max_length=100, null=True)),
                ('choice_name', models.CharField(blank=True, db_column='choiceName', max_length=100, null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('header_part', models.BooleanField(db_column='header_part', default=False)),
                ('body_part', models.BooleanField(db_column='body_part', default=False)),
                ('footer_part', models.BooleanField(db_column='footer_part', default=False)),
                ('mandatory', models.BooleanField(db_column='Mandatory', default=False)),
                ('image', models.ImageField(blank=True, db_column='image', null=True, upload_to='img')),
            ],
            options={
                'db_table': 'WebConsultation_AnalysisMaster',
            },
        ),
    ]
