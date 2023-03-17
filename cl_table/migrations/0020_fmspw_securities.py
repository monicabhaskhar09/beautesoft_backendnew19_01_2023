# Generated by Django 3.0.7 on 2020-10-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0019_auto_20201009_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fmspw',
            fields=[
                ('pw_id', models.AutoField(db_column='PW_ID', primary_key=True, serialize=False)),
                ('pw_userlogin', models.CharField(blank=True, db_column='PW_UserLogin', max_length=50, null=True)),
                ('pw_password', models.CharField(blank=True, db_column='PW_Password', max_length=15, null=True)),
                ('flgdisc', models.BooleanField()),
                ('level_itmid', models.IntegerField(blank=True, db_column='LEVEL_ItmID', null=True)),
                ('pw_isactive', models.BooleanField(db_column='PW_Isactive')),
                ('level_desc', models.CharField(blank=True, db_column='Level_Desc', max_length=50, null=True)),
                ('emp_code', models.CharField(blank=True, db_column='Emp_Code', max_length=20, null=True)),
                ('flgphy', models.BooleanField(db_column='flgPHY')),
                ('flggrn', models.BooleanField(db_column='flgGRN')),
                ('flgadj', models.BooleanField(db_column='flgADJ')),
                ('flgtfr', models.BooleanField(db_column='flgTFR')),
                ('flgdelart', models.BooleanField(db_column='flgDelArt')),
                ('flgmclock', models.BooleanField(db_column='flgMClock')),
                ('lallowflgdelart', models.BooleanField(db_column='lallowFlgDelArt')),
                ('flgopendrawer', models.BooleanField()),
                ('flgexchange', models.BooleanField(db_column='flgExchange')),
                ('flgrevtrm', models.BooleanField(db_column='flgRevTrm')),
                ('flgvoid', models.BooleanField(db_column='flgVoid')),
                ('flgrefund', models.BooleanField(db_column='flgRefund')),
                ('flgemail', models.BooleanField(db_column='flgEmail')),
                ('flgcustadd', models.BooleanField(blank=True, db_column='flgCustAdd', null=True)),
                ('flgviewcost', models.BooleanField(blank=True, db_column='flgViewCost', null=True)),
                ('flgfoc', models.BooleanField(db_column='flgFOC')),
                ('flgappt', models.BooleanField(db_column='flgAppt')),
                ('flgexpire', models.BooleanField(db_column='flgExpire')),
                ('flgviewath', models.BooleanField(db_column='flgViewAth')),
                ('flgaddath', models.BooleanField(db_column='flgAddAth')),
                ('flgeditath', models.BooleanField(db_column='flgEditAth')),
                ('flgrefundpp', models.BooleanField(db_column='flgRefundPP')),
                ('flgrefundcn', models.BooleanField(db_column='flgRefundCN')),
                ('flgattn', models.BooleanField(db_column='flgAttn')),
                ('flgchangeexpirydate', models.BooleanField(db_column='flgChangeExpiryDate')),
                ('flgoutletrequest', models.BooleanField(db_column='flgOutletRequest')),
                ('flgstockusagememo', models.BooleanField(db_column='flgStockUsageMemo')),
                ('flgappteditath', models.BooleanField(db_column='flgApptEditAth')),
                ('flgchangeunitprice', models.BooleanField(db_column='flgChangeUnitPrice')),
                ('flgoveridearstaff', models.BooleanField(db_column='flgOverideARStaff')),
                ('flgluckydraw', models.BooleanField(db_column='flgLuckyDraw')),
                ('flgaccountinterface', models.BooleanField(db_column='flgAccountInterface')),
                ('flgvoidcurrentday', models.BooleanField(db_column='flgVoidCurrentDay')),
                ('flgallowinsufficent', models.BooleanField(db_column='flgAllowInsufficent')),
                ('flgallowcardusage', models.BooleanField(db_column='flgAllowCardUsage')),
                ('flgallowblockappointment', models.BooleanField(db_column='flgAllowBlockAppointment')),
                ('flgalldayendsettlement', models.BooleanField(blank=True, db_column='flgAllDayEndSettlement', null=True)),
                ('flgallcom', models.BooleanField(blank=True, db_column='flgAllCom', null=True)),
                ('flgallowtdexpiryservice', models.BooleanField(db_column='flgAllowTDExpiryService')),
                ('salon_code', models.CharField(db_column='Salon_Code', max_length=40, null=True)),
            ],
            options={
                'db_table': 'FMSPW',
            },
        ),
        migrations.CreateModel(
            name='Securities',
            fields=[
                ('level_itmid', models.AutoField(db_column='LEVEL_ItmID', primary_key=True, serialize=False)),
                ('level_name', models.CharField(blank=True, db_column='LEVEL_Name', max_length=40, null=True)),
                ('level_description', models.CharField(blank=True, db_column='LEVEL_Description', max_length=60, null=True)),
                ('level_permitappointment', models.BooleanField(db_column='LEVEL_PermitAppointment')),
                ('level_permitcrm', models.BooleanField(db_column='LEVEL_PermitCrm')),
                ('level_permitcreditor', models.BooleanField(db_column='LEVEL_PermitCreditor')),
                ('level_permitstaff', models.BooleanField(db_column='LEVEL_PermitStaff')),
                ('level_permituserlogin', models.BooleanField(db_column='LEVEL_PermitUserLogin')),
                ('level_permitstockitem', models.BooleanField(db_column='LEVEL_PermitStockItem')),
                ('level_permitsecurity', models.BooleanField(db_column='LEVEL_PermitSecurity')),
                ('level_permitsendmail', models.BooleanField(db_column='LEVEL_PermitSendmail')),
                ('level_permitinventory', models.BooleanField(db_column='LEVEL_PermitInventory')),
                ('level_permitanalysis', models.BooleanField(db_column='LEVEL_PermitAnalysis')),
                ('level_permitmaintain', models.BooleanField(db_column='LEVEL_PermitMaintain')),
                ('level_permitpos', models.BooleanField(db_column='LEVEL_PermitPOS')),
                ('level_isactive', models.BooleanField(db_column='LEVEL_Isactive')),
                ('level_permitpaytable', models.BooleanField(db_column='LEVEL_PermitPaytable')),
                ('level_permitforex', models.BooleanField(db_column='LEVEL_PermitForex')),
                ('level_permitdiv', models.BooleanField(db_column='LEVEL_PermitDiv')),
                ('level_permitdiscount', models.BooleanField(db_column='LEVEL_PermitDiscount')),
                ('level_permitdept', models.BooleanField(db_column='LEVEL_PermitDept')),
                ('level_permitclass', models.BooleanField(db_column='LEVEL_PermitClass')),
                ('level_permitpromo', models.BooleanField(db_column='LEVEL_PermitPromo')),
                ('level_permitattendance', models.BooleanField(db_column='LEVEL_PermitAttendance')),
                ('level_permitstkreceive', models.BooleanField(db_column='LEVEL_PermitStkReceive')),
                ('level_permitstkadj', models.BooleanField(db_column='LEVEL_PermitStkAdj')),
                ('level_permitstktrans', models.BooleanField(db_column='LEVEL_PermitStkTrans')),
                ('level_permitstkwriteoff', models.BooleanField(db_column='LEVEL_PermitStkWriteOff')),
                ('level_permitstkquery', models.BooleanField(db_column='LEVEL_PermitStkQuery')),
                ('level_permitstktk', models.BooleanField(db_column='LEVEL_PermitStkTK')),
                ('level_permitstkvar', models.BooleanField(db_column='LEVEL_PermitStkVar')),
                ('level_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Securities',
            },
        ),
    ]
