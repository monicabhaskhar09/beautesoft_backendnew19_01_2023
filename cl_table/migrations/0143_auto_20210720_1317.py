# Generated by Django 3.0.7 on 2021-07-20 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0142_treatment_master_checktype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerformcontrol',
            name='Site_Codeid',
        ),
        migrations.DeleteModel(
            name='Multilanguage',
        ),
        migrations.AlterUniqueTogether(
            name='multilanguageword',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='multilanguageword',
            name='language',
        ),
        migrations.DeleteModel(
            name='CustomerFormControl',
        ),
        migrations.DeleteModel(
            name='MultiLanguageWord',
        ),
    ]