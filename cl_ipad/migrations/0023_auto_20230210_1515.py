# Generated by Django 3.0.7 on 2023-02-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0022_auto_20230203_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='webconsultation_questionsub_questions',
            name='answer',
            field=models.IntegerField(blank=True, db_column='answer', null=True),
        ),
        migrations.AddField(
            model_name='webconsultation_questionsub_questions',
            name='answer_text',
            field=models.CharField(blank=True, db_column='answerText', max_length=200, null=True),
        ),
    ]
