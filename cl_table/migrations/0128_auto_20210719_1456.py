# Generated by Django 3.0.7 on 2021-07-19 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0044_merge_20210717_2039'),
        ('cl_table', '0127_merge_20210719_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTitle',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=20, null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='ITM_DESC', max_length=20, null=True)),
                ('seq', models.FloatField(db_column='SEQ')),
                ('isactive', models.BooleanField(db_column='ISACTIVE')),
            ],
            options={
                'db_table': 'Customer_Title',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailysalestdSummary',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(db_column='SiteCode', max_length=20)),
                ('business_date', models.DateTimeField(db_column='Business_Date')),
                ('helper_code', models.CharField(blank=True, db_column='Helper_Code', max_length=20, null=True)),
                ('daily_share_count', models.FloatField(blank=True, db_column='Daily_Share_Count', null=True)),
                ('daily_share_amount', models.FloatField(blank=True, db_column='Daily_Share_Amount', null=True)),
                ('lastupdate', models.DateTimeField(db_column='LastUpDate')),
            ],
            options={
                'db_table': 'DailySalesTD_Summary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuSecurity',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('security_level_code', models.CharField(blank=True, db_column='SECURITY_LEVEL_CODE', max_length=20, null=True)),
                ('security_level_desc', models.CharField(blank=True, db_column='SECURITY_LEVEL_DESC', max_length=50, null=True)),
                ('is_active', models.BooleanField(db_column='IS_ACTIVE')),
            ],
            options={
                'db_table': 'Menu_Security',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuSecuritylevellist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('security_level_code', models.CharField(blank=True, db_column='SECURITY_LEVEL_CODE', max_length=20, null=True)),
                ('menu_list', models.CharField(blank=True, db_column='MENU_LIST', max_length=100, null=True)),
                ('menu_active', models.BooleanField(db_column='MENU_ACTIVE')),
            ],
            options={
                'db_table': 'Menu_SecurityLevelList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RedeemPolicy',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('redeem_code', models.CharField(db_column='Redeem_Code', max_length=20)),
                ('cust_type', models.CharField(db_column='Cust_Type', max_length=20)),
                ('cur_value', models.FloatField(db_column='Cur_Value')),
                ('point_value', models.FloatField(db_column='Point_Value')),
                ('isactive', models.BooleanField(db_column='IsActive')),
            ],
            options={
                'db_table': 'Redeem_Policy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RewardPolicy',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('reward_code', models.CharField(db_column='Reward_Code', max_length=20)),
                ('cust_type', models.CharField(db_column='Cust_Type', max_length=20)),
                ('cur_value', models.FloatField(db_column='Cur_Value')),
                ('point_value', models.FloatField(db_column='Point_Value')),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('reward_item_type', models.CharField(blank=True, db_column='Reward_Item_Type', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Reward_Policy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securitycontrollist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('controlname', models.CharField(blank=True, db_column='ControlName', max_length=50, null=True)),
                ('controldesc', models.CharField(blank=True, db_column='ControlDesc', max_length=50, null=True)),
                ('controlindex', models.IntegerField(blank=True, db_column='ControlIndex', null=True)),
                ('controlparent', models.CharField(blank=True, db_column='ControlParent', max_length=50, null=True)),
                ('control_status', models.BooleanField(blank=True, db_column='Control_Status', null=True)),
                ('seq', models.IntegerField(blank=True, db_column='SEQ', null=True)),
            ],
            options={
                'db_table': 'SecurityControlList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securitylevellist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('controlname', models.CharField(blank=True, db_column='ControlName', max_length=50, null=True)),
                ('controldesc', models.CharField(blank=True, db_column='ControlDesc', max_length=50, null=True)),
                ('controlparent', models.CharField(blank=True, db_column='ControlParent', max_length=50, null=True)),
                ('controlindex', models.IntegerField(blank=True, db_column='ControlIndex', null=True)),
                ('controlstatus', models.BooleanField(db_column='ControlStatus')),
                ('level_itemid', models.CharField(blank=True, db_column='Level_ItemID', max_length=50, null=True)),
                ('seq', models.CharField(blank=True, db_column='SEQ', max_length=10, null=True)),
            ],
            options={
                'db_table': 'SecurityLevelList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skillstaff',
            fields=[
                ('id', models.BigAutoField(db_column='Id', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(blank=True, db_column='siteCode', max_length=10, null=True)),
                ('staffcode', models.CharField(blank=True, db_column='staffCode', max_length=20, null=True)),
                ('itemcode', models.CharField(blank=True, db_column='itemCode', max_length=20, null=True)),
            ],
            options={
                'db_table': 'skillstaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailysalesdataDetail',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(db_column='SiteCode', max_length=20)),
                ('sales_date', models.DateTimeField(db_column='Sales_Date')),
                ('business_date', models.DateTimeField(db_column='Business_Date')),
                ('sa_transacno', models.CharField(blank=True, db_column='SA_TransacNo', max_length=20, null=True)),
                ('sa_transacno_ref', models.CharField(blank=True, db_column='SA_TransacNo_Ref', max_length=20, null=True)),
                ('version', models.CharField(blank=True, db_column='Version', max_length=20, null=True)),
                ('sales_gt1_withgst', models.FloatField(blank=True, db_column='Sales_GT1_WithGST', null=True)),
                ('sales_gt1_gst', models.FloatField(blank=True, db_column='Sales_GT1_GST', null=True)),
                ('sales_gt1_beforegst', models.FloatField(blank=True, db_column='Sales_GT1_BeforeGST', null=True)),
                ('servicesales_gt1', models.FloatField(blank=True, db_column='ServiceSales_GT1', null=True)),
                ('productsales_gt1', models.FloatField(blank=True, db_column='ProductSales_GT1', null=True)),
                ('prepaidsales_gt1', models.FloatField(blank=True, db_column='PrepaidSales_GT1', null=True)),
                ('sales_gt2_withgst', models.FloatField(blank=True, db_column='Sales_GT2_WithGST', null=True)),
                ('sales_gt2_gst', models.FloatField(blank=True, db_column='Sales_GT2_GST', null=True)),
                ('sales_gt2_beforegst', models.FloatField(blank=True, db_column='Sales_GT2_BeforeGST', null=True)),
                ('servicesales_gt2', models.FloatField(blank=True, db_column='ServiceSales_GT2', null=True)),
                ('productsales_gt2', models.FloatField(blank=True, db_column='ProductSales_GT2', null=True)),
                ('prepaidsales_gt2', models.FloatField(blank=True, db_column='PrepaidSales_GT2', null=True)),
                ('treatmentdoneqty', models.FloatField(blank=True, db_column='TreatmentDoneQty', null=True)),
                ('treatmentdoneamount', models.FloatField(blank=True, db_column='TreatmentDoneAmount', null=True)),
                ('lastupdate', models.DateTimeField(db_column='LastUpDate')),
                ('processlog_ref', models.CharField(blank=True, db_column='ProcessLog_Ref', max_length=20, null=True)),
                ('vouchersales_gt1', models.FloatField(blank=True, db_column='VoucherSales_GT1', null=True)),
                ('vouchersales_gt2', models.FloatField(blank=True, db_column='VoucherSales_GT2', null=True)),
            ],
            options={
                'db_table': 'DailySalesData_Detail',
            },
        ),
        migrations.CreateModel(
            name='DailysalesdataSummary',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(db_column='SiteCode', max_length=20)),
                ('business_date', models.DateTimeField(db_column='Business_Date')),
                ('version', models.CharField(db_column='Version', max_length=20)),
                ('sales_gt1_withgst', models.FloatField(blank=True, db_column='Sales_GT1_WithGST', null=True)),
                ('sales_gt1_gst', models.FloatField(blank=True, db_column='Sales_GT1_GST', null=True)),
                ('sales_gt1_beforegst', models.FloatField(blank=True, db_column='Sales_GT1_BeforeGST', null=True)),
                ('servicesales_gt1', models.FloatField(blank=True, db_column='ServiceSales_GT1', null=True)),
                ('productsales_gt1', models.FloatField(blank=True, db_column='ProductSales_GT1', null=True)),
                ('vouchersales_gt1', models.FloatField(blank=True, db_column='VoucherSales_GT1', null=True)),
                ('prepaidsales_gt1', models.FloatField(blank=True, db_column='PrepaidSales_GT1', null=True)),
                ('sales_gt2_withgst', models.FloatField(blank=True, db_column='Sales_GT2_WithGST', null=True)),
                ('sales_gt2_gst', models.FloatField(blank=True, db_column='Sales_GT2_GST', null=True)),
                ('sales_gt2_beforegst', models.FloatField(blank=True, db_column='Sales_GT2_BeforeGST', null=True)),
                ('servicesales_gt2', models.FloatField(blank=True, db_column='ServiceSales_GT2', null=True)),
                ('productsales_gt2', models.FloatField(blank=True, db_column='ProductSales_GT2', null=True)),
                ('vouchersales_gt2', models.FloatField(blank=True, db_column='VoucherSales_GT2', null=True)),
                ('prepaidsales_gt2', models.FloatField(blank=True, db_column='PrepaidSales_GT2', null=True)),
                ('treatmentdoneqty', models.FloatField(blank=True, db_column='TreatmentDoneQty', null=True)),
                ('treatmentdoneamount', models.FloatField(blank=True, db_column='TreatmentDoneAmount', null=True)),
                ('lastupdate', models.DateTimeField(db_column='LastUpDate')),
            ],
            options={
                'db_table': 'DailySalesData_Summary',
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('sys_code', models.AutoField(db_column='Sys_Code', primary_key=True, serialize=False)),
                ('diagnosis_date', models.DateTimeField(blank=True, db_column='Diagnosis_Date', null=True)),
                ('next_appt', models.DateTimeField(blank=True, db_column='Next_Appt', null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', max_length=255, null=True)),
                ('homecare', models.CharField(blank=True, db_column='HomeCare', max_length=255, null=True)),
                ('date_pic_take', models.DateTimeField(blank=True, db_column='Date_Pic_Take', null=True)),
                ('treatment_code', models.CharField(blank=True, db_column='Treatment_Code', max_length=50, null=True)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('cust_code', models.CharField(db_column='Cust_Code', max_length=50)),
                ('diagnosis_code', models.CharField(blank=True, db_column='Diagnosis_Code', max_length=50, null=True)),
                ('left_desc1', models.CharField(blank=True, db_column='Left_Desc1', max_length=100, null=True)),
                ('left_desc2', models.CharField(blank=True, db_column='Left_Desc2', max_length=100, null=True)),
                ('right_desc1', models.CharField(blank=True, db_column='Right_Desc1', max_length=100, null=True)),
                ('right_desc2', models.CharField(blank=True, db_column='Right_Desc2', max_length=100, null=True)),
                ('treatment_name', models.CharField(blank=True, db_column='Treatment_Name', max_length=50, null=True)),
                ('remark1', models.CharField(blank=True, db_column='Remark1', max_length=200, null=True)),
                ('remark2', models.CharField(blank=True, db_column='Remark2', max_length=200, null=True)),
                ('remark3', models.CharField(blank=True, db_column='Remark3', max_length=200, null=True)),
                ('remark4', models.CharField(blank=True, db_column='Remark4', max_length=200, null=True)),
                ('remark5', models.CharField(blank=True, db_column='Remark5', max_length=200, null=True)),
                ('remark6', models.CharField(blank=True, db_column='Remark6', max_length=200, null=True)),
                ('pic_path', models.ImageField(blank=True, db_column='PIC_path', max_length=255, null=True, upload_to='img')),
                ('pic_path2', models.ImageField(blank=True, db_column='PIC_Path2', max_length=255, null=True, upload_to='img')),
                ('pic_path3', models.ImageField(blank=True, db_column='PIC_Path3', max_length=255, null=True, upload_to='img')),
                ('pic_path4', models.ImageField(blank=True, db_column='PIC_Path4', max_length=255, null=True, upload_to='img')),
                ('pic_path5', models.ImageField(blank=True, db_column='PIC_Path5', max_length=255, null=True, upload_to='img')),
                ('pic_path6', models.ImageField(blank=True, db_column='PIC_Path6', max_length=255, null=True, upload_to='img')),
                ('pic1', models.BinaryField(blank=True, db_column='PIC1', null=True)),
                ('pic2', models.BinaryField(blank=True, db_column='PIC2', null=True)),
                ('pic3', models.BinaryField(blank=True, db_column='PIC3', null=True)),
                ('pic4', models.BinaryField(blank=True, db_column='PIC4', null=True)),
                ('pic5', models.BinaryField(blank=True, db_column='PIC5', null=True)),
                ('pic6', models.BinaryField(blank=True, db_column='PIC6', null=True)),
                ('site_code', models.CharField(db_column='Site_Code', max_length=50)),
            ],
            options={
                'db_table': 'Diagnosis',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_desc', models.CharField(blank=True, db_column='ITM_DESC', max_length=40, null=True)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=40, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Language',
            },
        ),
        migrations.CreateModel(
            name='Multilanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('english', models.CharField(blank=True, max_length=250, null=True)),
                ('zh_sg', models.CharField(blank=True, db_column='zh-sg', max_length=250, null=True)),
            ],
            options={
                'db_table': 'MultiLanguage',
            },
        ),
        migrations.RemoveField(
            model_name='postaud',
            name='gt',
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_consultant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_consultant', to='cl_table.Employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_therapist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_therapist', to='cl_table.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Country'),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_remarks',
            field=models.CharField(blank=True, db_column='Emp_remarks', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='schedulehour',
            name='shortdesc',
            field=models.CharField(db_column='shortDesc', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='holditemdetail',
            name='status',
            field=models.CharField(blank=True, choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE'), ('VOID', 'VOID')], db_column='Status', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stktrn',
            name='trn_date',
            field=models.DateTimeField(auto_now=True, db_column='TRN_DATE', null=True),
        ),
        migrations.AlterField(
            model_name='stktrn',
            name='trn_post',
            field=models.DateTimeField(auto_now=True, db_column='TRN_POST', null=True),
        ),
        migrations.AlterField(
            model_name='treatment_master',
            name='checktype',
            field=models.CharField(blank=True, choices=[('service', 'service'), ('package', 'package'), ('freetext', 'freetext')], db_column='CheckType', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='DiagnosisCompare',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('compare_code', models.CharField(blank=True, db_column='Compare_Code', max_length=100, null=True)),
                ('compare_remark', models.TextField(blank=True, db_column='Compare_Remark', null=True)),
                ('compare_datetime', models.DateTimeField(blank=True, db_column='Compare_DateTime', null=True)),
                ('compare_isactive', models.BooleanField(db_column='Compare_IsActive', default=True)),
                ('compare_user', models.CharField(blank=True, db_column='Compare_User', max_length=20, null=True)),
                ('cust_code', models.CharField(blank=True, db_column='Cust_Code', max_length=50, null=True)),
                ('diagnosis1_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis_compare_1', to='cl_table.Diagnosis')),
                ('diagnosis2_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis_compare_2', to='cl_table.Diagnosis')),
            ],
            options={
                'db_table': 'Diagnosis_Compare',
            },
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='cust_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer'),
        ),
        migrations.CreateModel(
            name='CustomerPointDtl',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('transacno', models.CharField(db_column='TransacNo', max_length=20)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('cust_code', models.CharField(db_column='Cust_Code', max_length=20)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('parent_code', models.CharField(blank=True, db_column='Parent_Code', max_length=20, null=True)),
                ('parent_desc', models.CharField(blank=True, db_column='Parent_Desc', max_length=50, null=True)),
                ('parent_display', models.CharField(blank=True, db_column='Parent_Display', max_length=100, null=True)),
                ('itm_code', models.CharField(blank=True, db_column='itm_Code', max_length=20, null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='itm_Desc', max_length=50, null=True)),
                ('point', models.FloatField(db_column='Point')),
                ('now_point', models.FloatField(db_column='Now_Point')),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=100, null=True)),
                ('remark_code', models.CharField(blank=True, db_column='Remark_Code', max_length=20, null=True)),
                ('remark_desc', models.CharField(blank=True, db_column='Remark_Desc', max_length=50, null=True)),
                ('isvoid', models.BooleanField(db_column='Isvoid')),
                ('void_referenceno', models.CharField(blank=True, db_column='void_ReferenceNo', max_length=20, null=True)),
                ('isopen', models.BooleanField(blank=True, db_column='IsOpen', null=True)),
                ('qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
                ('total_point', models.FloatField(blank=True, db_column='Total_Point', null=True)),
                ('seq', models.IntegerField(blank=True, db_column='Seq', null=True)),
                ('sa_status', models.CharField(blank=True, db_column='Sa_status', max_length=10, null=True)),
                ('bal_acc2', models.FloatField(blank=True, db_column='Bal_Acc2', null=True)),
                ('point_acc1', models.FloatField(blank=True, db_column='Point_Acc1', null=True)),
                ('point_acc2', models.FloatField(blank=True, db_column='Point_Acc2', null=True)),
                ('locid', models.CharField(db_column='LocID', max_length=50)),
            ],
            options={
                'db_table': 'Customer_Point_Dtl',
                'unique_together': {('transacno', 'cust_code', 'point', 'now_point', 'locid')},
            },
        ),
        migrations.CreateModel(
            name='CustomerPoint',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('transacno', models.CharField(db_column='TransacNO', max_length=20)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=100, null=True)),
                ('time', models.DateTimeField(blank=True, db_column='Time', null=True)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('cust_code', models.CharField(db_column='Cust_Code', max_length=100)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=20, null=True)),
                ('refno', models.CharField(db_column='RefNo', max_length=20)),
                ('ref_source', models.CharField(db_column='Ref_Source', max_length=50)),
                ('isvoid', models.BooleanField(db_column='Isvoid')),
                ('sa_status', models.CharField(db_column='Sa_Status', max_length=10)),
                ('void_referenceno', models.CharField(blank=True, db_column='void_ReferenceNo', max_length=20, null=True)),
                ('total_point', models.FloatField(db_column='Total_Point')),
                ('now_point', models.FloatField(blank=True, db_column='Now_Point', null=True)),
                ('seq', models.IntegerField(blank=True, db_column='Seq', null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', max_length=10, null=True)),
                ('bal_point', models.FloatField(db_column='Bal_Point')),
                ('expired', models.BooleanField(db_column='Expired')),
                ('expired_date', models.DateTimeField(blank=True, db_column='Expired_Date', null=True)),
                ('mac_code', models.CharField(db_column='Mac_Code', max_length=100)),
                ('logno', models.CharField(db_column='LogNo', max_length=100)),
                ('approval_user', models.CharField(db_column='Approval_User', max_length=100)),
                ('cardno', models.CharField(db_column='CardNo', max_length=100)),
                ('bdate', models.DateTimeField(blank=True, db_column='BDate', null=True)),
                ('pdate', models.DateTimeField(blank=True, db_column='PDate', null=True)),
                ('expired_point', models.FloatField()),
                ('postransactionno', models.CharField(db_column='posTransactionNo', max_length=50)),
                ('postotalamt', models.FloatField(blank=True, db_column='posTotalAmt', null=True)),
                ('locid', models.CharField(db_column='LocID', max_length=50)),
                ('mgm_refno', models.CharField(blank=True, db_column='MGM_RefNo', max_length=20, null=True)),
                ('tdate', models.CharField(blank=True, db_column='TDate', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Customer_Point',
                'unique_together': {('transacno', 'cust_code', 'sa_status', 'total_point', 'postransactionno', 'locid')},
            },
        ),
        migrations.CreateModel(
            name='CustomerFormControl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(blank=True, db_column='fieldName', max_length=50, null=True)),
                ('display_field_name', models.CharField(blank=True, db_column='displayFieldName', max_length=50, null=True)),
                ('visible_in_registration', models.BooleanField(db_column='visibleInRegistration')),
                ('visible_in_listing', models.BooleanField(db_column='visibleInListing')),
                ('visible_in_profile', models.BooleanField(db_column='visibleInProfile')),
                ('editable', models.BooleanField()),
                ('mandatory', models.BooleanField()),
                ('order', models.IntegerField()),
                ('col_width', models.IntegerField(default=6)),
                ('isActive', models.BooleanField(db_column='isActive')),
                ('Site_Codeid', models.ForeignKey(db_column='Site_Codeid_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_form_control', to='cl_app.ItemSitelist')),
            ],
            options={
                'db_table': 'customerFormControl',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='Cust_titleid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.CustomerTitle'),
        ),
        migrations.CreateModel(
            name='MultiLanguageWord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wordCode', models.IntegerField()),
                ('word', models.CharField(max_length=250)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cl_table.Language')),
            ],
            options={
                'db_table': 'MultiLanguageWord',
                'unique_together': {('wordCode', 'language')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='diagnosis',
            unique_together={('sys_code', 'cust_no', 'site_code')},
        ),
    ]