# Generated by Django 3.0.7 on 2021-05-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0026_itemcart_multistaff_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='itemtype',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='recorddetail',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
