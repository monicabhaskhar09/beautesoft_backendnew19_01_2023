# Generated by Django 3.0.7 on 2020-10-09 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0002_auto_20201009_0613'),
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplevel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='emplevel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='holditemsetup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='holditemsetup',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='additional_discount',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='additional_discountamt',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='auto',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='cart_date',
            field=models.DateField(db_column='Cart_Date', null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='cart_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='cart_status',
            field=models.CharField(choices=[('Inprogress', 'Inprogress'), ('Suspension', 'Suspension'), ('Completed', 'Completed')], db_column='Cart_Status', default='Inprogress', max_length=20),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='check',
            field=models.CharField(choices=[('New', 'New'), ('Old', 'Old')], db_column='Check', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='deposit',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='disc_reason',
            field=models.ManyToManyField(blank=True, to='custom.PaymentRemarks'),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='discount',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='discount_amt',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='discount_price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='discreason_txt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='holditemqty',
            field=models.IntegerField(db_column='HoldItemQty', null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='holdreason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.HolditemSetup'),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='is_payment',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='lineno',
            field=models.IntegerField(db_column='LineNo', null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='ratio',
            field=models.DecimalField(db_column='Ratio', decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='remark',
            field=models.CharField(db_column='Remark', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='sa_transacno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='sitecodeid',
            field=models.ForeignKey(db_column='sitecodeid', null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='tax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='total_price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='trans_amt',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='itemcart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentremarks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentremarks',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Room_PIC',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='room',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='equipmentpicturelocation',
            field=models.CharField(blank=True, db_column='equipmentPictureLocation', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='roomtype',
            field=models.CharField(blank=True, db_column='roomType', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='roundpoint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='roundpoint',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='roundsales',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='roundsales',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='voucherrecord',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='voucherrecord',
            name='isvalid',
            field=models.BooleanField(db_column='isValid', default=True),
        ),
        migrations.AddField(
            model_name='voucherrecord',
            name='site_codeid',
            field=models.ForeignKey(db_column='Site_Codeid', null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='voucherrecord',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='emplevel',
            name='level_isactive',
            field=models.BooleanField(db_column='Level_IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='emplevel',
            name='level_spa',
            field=models.BooleanField(db_column='Level_SPA', null=True),
        ),
        migrations.AlterField(
            model_name='itemcart',
            name='isactive',
            field=models.BooleanField(blank=True, db_column='isActive', default=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentremarks',
            name='isactive',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='isactive',
            field=models.BooleanField(blank=True, db_column='Isactive', default=True, null=True),
        ),
    ]
