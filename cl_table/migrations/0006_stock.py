# Generated by Django 3.0.7 on 2020-10-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0005_auto_20201009_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('item_no', models.AutoField(db_column='Item_no', primary_key=True, serialize=False)),
                ('item_code', models.CharField(blank=True, max_length=20, null=True)),
                ('itm_icid', models.FloatField(blank=True, db_column='Itm_ICID', null=True)),
                ('itm_code', models.CharField(blank=True, db_column='Itm_Code', max_length=20, null=True)),
                ('item_div', models.CharField(blank=True, db_column='Item_Div', max_length=20, null=True)),
                ('item_dept', models.CharField(blank=True, db_column='Item_Dept', max_length=20, null=True)),
                ('item_class', models.CharField(blank=True, db_column='Item_Class', max_length=20, null=True)),
                ('item_barcode', models.CharField(blank=True, db_column='Item_Barcode', max_length=20, null=True)),
                ('onhand_cst', models.FloatField(blank=True, db_column='ONHAND_CST', null=True)),
                ('item_margin', models.FloatField(blank=True, db_column='Item_Margin', null=True)),
                ('item_isactive', models.BooleanField()),
                ('item_name', models.CharField(blank=True, db_column='Item_Name', max_length=60, null=True)),
                ('item_abbc', models.CharField(blank=True, db_column='Item_abbc', max_length=60, null=True)),
                ('item_desc', models.CharField(blank=True, db_column='Item_Desc', max_length=60, null=True)),
                ('cost_price', models.DecimalField(blank=True, db_column='COST_PRICE', decimal_places=4, max_digits=19, null=True)),
                ('item_price', models.DecimalField(blank=True, db_column='Item_Price', decimal_places=4, max_digits=19, null=True)),
                ('onhand_qty', models.FloatField(blank=True, db_column='ONHAND_QTY', null=True)),
                ('itm_promotionyn', models.CharField(blank=True, db_column='Itm_PromotionYN', max_length=20, null=True)),
                ('itm_disc', models.FloatField(blank=True, db_column='Itm_Disc', null=True)),
                ('itm_commission', models.FloatField(blank=True, db_column='Itm_Commission', null=True)),
                ('item_type', models.CharField(blank=True, db_column='Item_Type', max_length=20, null=True)),
                ('itm_duration', models.FloatField(blank=True, db_column='Itm_Duration', null=True)),
                ('item_price2', models.FloatField(blank=True, db_column='Item_Price2', null=True)),
                ('item_price3', models.FloatField(blank=True, db_column='Item_Price3', null=True)),
                ('item_price4', models.FloatField(blank=True, db_column='Item_Price4', null=True)),
                ('item_price5', models.FloatField(blank=True, db_column='Item_Price5', null=True)),
                ('itm_remark', models.CharField(blank=True, db_column='Itm_Remark', max_length=100, null=True)),
                ('itm_value', models.CharField(blank=True, db_column='Itm_Value', max_length=10, null=True)),
                ('itm_expiredate', models.DateTimeField(blank=True, db_column='Itm_ExpireDate', null=True)),
                ('itm_status', models.CharField(blank=True, db_column='Itm_Status', max_length=10, null=True)),
                ('item_minqty', models.IntegerField(blank=True, null=True)),
                ('item_maxqty', models.IntegerField(blank=True, null=True)),
                ('item_onhandcost', models.CharField(blank=True, db_column='item_OnHandCost', max_length=20, null=True)),
                ('item_barcode1', models.CharField(blank=True, db_column='item_Barcode1', max_length=20, null=True)),
                ('item_barcode2', models.CharField(blank=True, db_column='item_Barcode2', max_length=20, null=True)),
                ('item_barcode3', models.CharField(blank=True, db_column='item_Barcode3', max_length=20, null=True)),
                ('item_marginamt', models.FloatField(blank=True, null=True)),
                ('item_date', models.DateTimeField(blank=True, null=True)),
                ('item_time', models.DateTimeField(blank=True, null=True)),
                ('item_moddate', models.DateTimeField(blank=True, db_column='item_ModDate', null=True)),
                ('item_modtime', models.DateTimeField(blank=True, db_column='item_ModTime', null=True)),
                ('item_createuser', models.CharField(blank=True, max_length=60, null=True)),
                ('item_supp', models.CharField(blank=True, max_length=10, null=True)),
                ('item_parentcode', models.CharField(blank=True, db_column='Item_Parentcode', max_length=20, null=True)),
                ('item_color', models.CharField(blank=True, max_length=10, null=True)),
                ('item_sizepack', models.CharField(blank=True, db_column='item_SizePack', max_length=10, null=True)),
                ('item_size', models.CharField(blank=True, db_column='item_Size', max_length=10, null=True)),
                ('item_season', models.CharField(blank=True, db_column='item_Season', max_length=10, null=True)),
                ('item_fabric', models.CharField(blank=True, max_length=10, null=True)),
                ('item_brand', models.CharField(blank=True, db_column='item_Brand', max_length=10, null=True)),
                ('lstpo_ucst', models.FloatField(blank=True, db_column='LSTPO_UCST', null=True)),
                ('lstpo_no', models.CharField(blank=True, db_column='LSTPO_NO', max_length=20, null=True)),
                ('lstpo_date', models.DateTimeField(blank=True, db_column='LSTPO_Date', null=True)),
                ('item_havechild', models.BooleanField(db_column='item_haveChild')),
                ('value_applytochild', models.BooleanField(db_column='Value_ApplyToChild')),
                ('package_disc', models.FloatField(blank=True, db_column='Package_Disc', null=True)),
                ('have_package_disc', models.BooleanField(db_column='Have_Package_Disc')),
                ('pic_path', models.CharField(blank=True, db_column='PIC_Path', max_length=255, null=True)),
                ('item_foc', models.BooleanField(db_column='Item_FOC')),
                ('item_uom', models.CharField(blank=True, db_column='Item_UOM', max_length=20, null=True)),
                ('mixbrand', models.BooleanField(db_column='MIXBRAND')),
                ('serviceretail', models.BooleanField(blank=True, db_column='SERVICERETAIL', null=True)),
                ('item_range', models.CharField(blank=True, db_column='Item_Range', max_length=20, null=True)),
                ('commissionable', models.BooleanField(blank=True, db_column='Commissionable', null=True)),
                ('trading', models.BooleanField(blank=True, db_column='Trading', null=True)),
                ('cust_replenish_days', models.CharField(blank=True, db_column='Cust_Replenish_Days', max_length=10, null=True)),
                ('cust_advance_days', models.CharField(blank=True, db_column='Cust_Advance_Days', max_length=10, null=True)),
                ('salescomm', models.CharField(blank=True, db_column='SalesComm', max_length=20, null=True)),
                ('workcomm', models.CharField(blank=True, db_column='WorkComm', max_length=20, null=True)),
                ('reminder_active', models.BooleanField(blank=True, db_column='Reminder_Active', null=True)),
                ('disclimit', models.FloatField(blank=True, db_column='DiscLimit', null=True)),
                ('disctypeamount', models.BooleanField(blank=True, db_column='DiscTypeAmount', null=True)),
                ('autocustdisc', models.BooleanField(db_column='AutoCustDisc')),
                ('reorder_active', models.BooleanField(blank=True, db_column='ReOrder_Active', null=True)),
                ('reorder_minqty', models.FloatField(blank=True, db_column='ReOrder_MinQty', null=True)),
                ('service_expire_active', models.BooleanField(db_column='Service_Expire_Active')),
                ('service_expire_month', models.FloatField(blank=True, db_column='Service_Expire_Month', null=True)),
                ('treatment_limit_active', models.BooleanField(db_column='Treatment_Limit_Active')),
                ('treatment_limit_count', models.FloatField(blank=True, db_column='Treatment_Limit_Count', null=True)),
                ('limitservice_flexionly', models.BooleanField(db_column='LimitService_FlexiOnly')),
                ('salescommpoints', models.FloatField(blank=True, db_column='SalesCommPoints', null=True)),
                ('workcommpoints', models.FloatField(blank=True, db_column='WorkCommPoints', null=True)),
                ('item_price_floor', models.FloatField(blank=True, db_column='Item_Price_Floor', null=True)),
                ('voucher_value', models.FloatField(blank=True, db_column='Voucher_Value', null=True)),
                ('voucher_value_is_amount', models.BooleanField(db_column='Voucher_Value_Is_Amount')),
                ('voucher_valid_period', models.CharField(blank=True, db_column='Voucher_Valid_Period', max_length=20, null=True)),
                ('prepaid_value', models.FloatField(blank=True, db_column='Prepaid_Value', null=True)),
                ('prepaid_sell_amt', models.FloatField(blank=True, db_column='Prepaid_Sell_Amt', null=True)),
                ('prepaid_valid_period', models.CharField(blank=True, db_column='Prepaid_Valid_Period', max_length=20, null=True)),
                ('membercardnoaccess', models.BooleanField(blank=True, db_column='MemberCardNoAccess', null=True)),
                ('rpt_code', models.CharField(blank=True, db_column='Rpt_Code', max_length=20, null=True)),
                ('is_gst', models.BooleanField(db_column='IS_GST')),
                ('account_code', models.CharField(blank=True, db_column='Account_Code', max_length=20, null=True)),
                ('stock_pic_b', models.BinaryField(blank=True, db_column='Stock_PIC_B', null=True)),
                ('is_open_prepaid', models.BooleanField(db_column='IS_OPEN_PREPAID')),
                ('appt_wd_min', models.FloatField(blank=True, db_column='Appt_WD_Min', null=True)),
                ('service_cost', models.FloatField(blank=True, db_column='Service_Cost', null=True)),
                ('service_cost_percent', models.BooleanField(db_column='Service_Cost_Percent')),
                ('account_code_td', models.CharField(blank=True, db_column='Account_Code_TD', max_length=20, null=True)),
                ('voucher_isvalid_until_date', models.BooleanField(db_column='Voucher_IsValid_Until_Date')),
                ('voucher_valid_until_date', models.DateTimeField(blank=True, db_column='Voucher_Valid_Until_Date', null=True)),
                ('equipmentcost', models.FloatField(blank=True, null=True)),
                ('is_have_tax', models.BooleanField(db_column='IS_HAVE_TAX')),
                ('is_allow_foc', models.BooleanField(db_column='IS_ALLOW_FOC')),
                ('vilidity_from_date', models.DateTimeField(blank=True, db_column='Vilidity_From_Date', null=True)),
                ('vilidity_to_date', models.DateTimeField(blank=True, db_column='Vilidity_To_date', null=True)),
                ('vilidity_from_time', models.DateTimeField(blank=True, db_column='Vilidity_From_Time', null=True)),
                ('vilidity_to_time', models.DateTimeField(blank=True, db_column='Vilidity_To_Time', null=True)),
                ('t1_tax_code', models.CharField(blank=True, db_column='T1_Tax_Code', max_length=20, null=True)),
                ('t2_tax_code', models.CharField(blank=True, db_column='T2_Tax_Code', max_length=20, null=True)),
                ('prepaid_disc_type', models.CharField(blank=True, db_column='Prepaid_Disc_Type', max_length=20, null=True)),
                ('prepaid_disc_percent', models.FloatField(blank=True, db_column='Prepaid_Disc_Percent', null=True)),
                ('srv_duration', models.FloatField(blank=True, db_column='Srv_Duration', null=True)),
                ('voucher_template_name', models.CharField(blank=True, db_column='Voucher_Template_Name', max_length=50, null=True)),
                ('autoproportion', models.BooleanField(db_column='AutoProportion')),
                ('item_pingying', models.CharField(db_column='Item_PingYing', max_length=250, null=True)),
                ('process_remark', models.CharField(db_column='Process_Remark', max_length=250, null=True)),
            ],
            options={
                'db_table': 'Stock',
            },
        ),
    ]
