# Generated by Django 3.0.7 on 2020-10-09 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0002_auto_20201009_0613'),
        ('custom', '0002_auto_20201009_0626'),
        ('cl_table', '0022_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='EMP_TYPEid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.EmpLevel'),
        ),
        migrations.AddField(
            model_name='employee',
            name='LEVEL_ItmIDid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Securities'),
        ),
        migrations.AddField(
            model_name='employee',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff_emp', to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='defaultSiteCodeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff', to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='employee',
            name='fcmtoken',
            field=models.TextField(blank=True, db_column='FCMToken', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_login',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], db_column='Login', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='leave_bal',
            field=models.IntegerField(blank=True, db_column='Leave_bal', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='leave_taken',
            field=models.IntegerField(blank=True, db_column='Leave_taken', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='notificationsetting',
            field=models.BooleanField(blank=True, db_column='notificationSetting', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='otp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pw_password',
            field=models.CharField(db_column='PW_Password', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='skills_list',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='skillset',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age_range0',
            field=models.BooleanField(db_column='Age_Range0', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age_range1',
            field=models.BooleanField(db_column='Age_Range1', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age_range2',
            field=models.BooleanField(db_column='Age_Range2', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age_range3',
            field=models.BooleanField(db_column='Age_Range3', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age_range4',
            field=models.BooleanField(db_column='Age_Range4', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_dob',
            field=models.DateField(blank=True, db_column='Emp_DOB', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_email',
            field=models.EmailField(blank=True, db_column='Emp_email', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_isactive',
            field=models.BooleanField(db_column='Emp_isactive', default=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_joindate',
            field=models.DateField(blank=True, db_column='Emp_JoinDate', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_pic',
            field=models.ImageField(blank=True, db_column='Emp_PIC', null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='getsms',
            field=models.BooleanField(db_column='GetSMS', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='show_in_appt',
            field=models.BooleanField(db_column='Show_In_Appt', default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='show_in_sales',
            field=models.BooleanField(db_column='Show_In_Sales', default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='show_in_trmt',
            field=models.BooleanField(db_column='Show_In_Trmt', default=False, null=True),
        ),
    ]