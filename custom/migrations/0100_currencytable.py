# Generated by Django 3.0.7 on 2022-06-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0099_auto_20220613_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currencytable',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('curr_code', models.CharField(blank=True, db_column='Curr_Code', max_length=3, null=True)),
                ('curr_name', models.CharField(blank=True, db_column='Curr_Name', max_length=16, null=True)),
                ('curr_rate', models.DecimalField(blank=True, db_column='Curr_Rate', decimal_places=1, max_digits=2, null=True)),
                ('curr_isactive', models.IntegerField(blank=True, db_column='Curr_isactive', null=True)),
            ],
            options={
                'db_table': 'CurrencyTable',
            },
        ),
    ]
