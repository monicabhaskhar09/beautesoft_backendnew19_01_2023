from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r'termsandcondition', views.TermsandconditionViewset, basename='termsandcondition')
router.register(r'participants', views.ParticipantsViewset, basename='participants')
router.register(r'dayendconfirmlog', views.DayendconfirmlogViewset, basename='dayendconfirmlog')
router.register(r'customerpointsaccount', views.CustomerPointsAccountViewset, basename='customerpointsaccount')
router.register(r'mgmpolicycloud', views.MGMPolicyCloudViewset, basename='mgmpolicycloud')
router.register(r'customerreferral', views.CustomerReferralViewset, basename='customerreferral')
router.register(r'sitelistip', views.SitelistipViewset, basename='sitelistip')
router.register(r'displaycatalog', views.DisplayCatalogViewset, basename='displaycatalog')
router.register(r'displayItems', views.DisplayItemViewset, basename='displayItems')
router.register(r'outletrequestcustomer', views.OutletRequestCustomerViewset, basename='outletrequestcustomer')
router.register(r'manualrewardpoint', views.ManualRewardPointCustomerViewset, basename='manualrewardpoint')
router.register(r'onlinebooking', views.OnlineBookingDateSlotsViewset, basename='onlinebooking')
router.register(r'invoicetemplateconfig', views.InvoiceTemplateConfigViewset, basename='invoicetemplateconfig')
router.register(r'appointbooking', views.AppointBookingDateSlotsViewset, basename='appointbooking')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login', views.UserLoginAPIView.as_view(), name='login'),
    path('api/logout', views.UserLogoutAPIView.as_view(), name='logout'),
    path('api/employeebranchwise', views.EmployeeList.as_view(), name='employee-branch'),
    path('api/skills', views.ServicesListAPIView.as_view(), name='skills'),
    path('api/shiftlist', views.ShiftListAPIView.as_view(), name='shiftlist'),
    path('api/customers/all/', views.CustomerListAPIView.as_view(), name='customer_all'),
    path('api/bookingstatus/', views.AppointmentBookingStatusList.as_view(), name='bookingstatus'),
    path('api/branchlist/', views.ItemSiteListAPIView.as_view(), name='branchlist'),
    path('api/branchlogin/', views.ItemSiteListAPIViewLogin.as_view(), name='branchlogin'),
    path('api/treatmentstock/<int:pk>/', views.StockDetail.as_view(), name='treatmentstock'),
    path('api/staffsavailable/', views.StaffsAvailable.as_view(), name='staffsavailable'),
    path('api/userlist/', views.UsersList.as_view(), name='userlist'),
    path('api/paytable/', views.PaytableListAPIView.as_view(), name='paytable'),
    path('api/customerreceiptprint/', views.CustomerReceiptPrintList.as_view(), name='customerreceiptprint'),
    path('api/source/', views.SourceAPI.as_view(), name='source'),
    path('api/state/', views.StateAPI.as_view(), name='state'),
    path('api/country/', views.CountryAPI.as_view(), name='country'),
    path('api/language/', views.LanguageAPI.as_view(), name='language'),
    path('api/securities/', views.SecuritiesAPIView.as_view(), name='securities'),
    path('api/schedulehour/', views.ScheduleHourAPIView.as_view(), name='schedulehour'),
    path('api/custappt/', views.CustApptAPI.as_view(), name='custappt'),
    path('api/appttype/', views.ApptTypeAPIView.as_view(), name='appttype'),
    path('api/focreason/', views.FocReasonAPIView.as_view(), name='focreason'),
    # path('api/updatetable/', views.UpdateTablesAPIView.as_view(), name='updatetable'),
    path('api/treatmentpackages/', views.TreatmentApptAPI.as_view(), name='treatmentpackages'),
    path('api/appointmentsort/', views.AppointmentSortAPIView.as_view(), name='appointmentsort'),
    path('api/appttreatmentdonehistory/', views.ApptTreatmentDoneHistoryAPI.as_view(), name='appttreatmentdonehistory'),
    path('api/upcomingappointment/', views.UpcomingAppointmentAPIView.as_view(), name='upcomingappointment'),
    path('api/blockreason/', views.BlockReasonAPIView.as_view(), name='blockreason'),
    path('api/appointmentlistpdf/', views.AppointmentListPdf.as_view(), name='appointmentlistpdf'),
    path('api/dayendlist/', views.DayEndListAPIView.as_view(), name='dayendlist'),
    path('api/appointmentlog/', views.AppointmentLogAPIView.as_view(), name='appointmentlog'),
    path('api/custapptupcoming/', views.CustApptUpcomingAPIView.as_view(), name='custapptupcoming'),
    path('api/attendancestaff/', views.AttendanceStaffsAPIView.as_view(), name='attendancestaff'),
    path('api/meta/race/', views.meta_race, name='meta_race'),
    path('api/meta/nationality/', views.meta_nationality, name='meta_nationality'),
    path('api/meta/religion/', views.meta_religious, name='meta_religious'),
    path('api/meta/country/', views.meta_country, name='meta_country'),
    path('api/RewardItemList/', views.RewardItemList, name='RewardItemList'),
    path('api/CustomerClassList/', views.CustomerClassList, name='CustomerClassList'),
    path('api/WorkScheduleMonth/', views.MonthlyWorkSchedule.as_view(), name='WorkScheduleMonth'),
    path('api/MonthlyAllSchedule/', views.MonthlyAllSchedule.as_view(), name='MonthlyAllSchedule'),
    path('api/WorkScheduleHours/', views.schedule_hours, name='WorkScheduleHours'),
    path('api/SkillsItemTypeList/', views.SkillsItemTypeList, name='SkillsItemTypeList'),
    path('api/SkillsView/', views.SkillsView.as_view(), name='SkillsView'),
    path('api/PhotoDiagnosis/', views.PhotoDiagnosis.as_view(), name='PhotoDiagnosis'),
    path('api/PhotoDiagnosis/<int:id>/', views.PhotoDiagnosisDetail.as_view(), name='PhotoDiagnosisDetail'),
    path('api/DiagnosisCompare/', views.DiagnosisCompareView.as_view(), name='DiagnosisCompare'),
    path('api/DiagnosisCompare/<int:id>/', views.DiagnosisCompareViewDetail.as_view(), name='DiagnosisCompareViewDetail'),

    path('api/EmployeeSkills/', views.EmployeeSkillView.as_view(), name='EmployeeSkillView'),
    path('api/CustomerFormSettings/', views.CustomerFormSettingsView.as_view(), name='CustomerFormSettingsView'),
    path('api/CustomerFormSettings/details', views.CustomerFormSettings, name='CustomerFormSettingsDetails'),
    # path('api/RewardPolicy/', views.RewardPolicyView.as_view(), name='RewardPolicyView'),
    # path('api/RedeemPolicy/', views.RedeemPolicyView.as_view(), name='RedeemPolicyView'),
    path('api/EmployeeSecuritySettings/', views.EmployeeSecuritySettings.as_view(), name='EmployeeSecuritySettings'),
    path('api/IndividualEmpSettings/<int:emp_no>', views.IndividualEmpSettings.as_view(), name='IndividualEmpSettings'),
    path('api/EmployeeLevelsSettings/', views.EmployeeLevelsSettings, name='EmployeeLevelsSettings'),
    path('api/MultiLanguage/', views.MultiLanguage.as_view(), name='MultiLanguage'),
    path('api/MultiLanguageList/', views.MultiLanguage_list, name='MultiLanguage_list'),
    path('api/EmployeeLevels/', views.EmployeeLevels, name='EmployeeLevels'),
    path('api/DailySales/', views.DailySalesView.as_view(), name='DailySales'),
    path('api/DailySalesSummery/', views.DailySalesSummeryView.as_view(), name='DailySalesSummeryView'),
    path('api/MonthlySalesSummery/', views.MonthlySalesSummeryView.as_view(), name='MonthlySalesSummeryView'),
    path('api/DailySalesBySite/', views.DailySalesSummeryBySiteView.as_view(), name='DailySalesSummeryBySiteView'),
    path('api/MonthlySalesBySite/', views.MonthlySalesSummeryBySiteView.as_view(), name='MonthlySalesSummeryBySiteView'),
    path('api/DailySalesByConsultant/', views.DailySalesSummeryByConsultantView.as_view(), name='DailySalesSummeryByConsultantView'),
    path('api/ServicesByOutlet/', views.ServicesByOutletView.as_view(), name='ServicesByOutletView'),
    path('api/ProductByOutlet/', views.ProductByOutletView.as_view(), name='ProductByOutletView'),
    path('api/RankingByOutlet/', views.RankingByOutletView.as_view(), name='RankingByOutletView'),
    path('api/ServicesByConsultant/', views.ServicesByConsultantView.as_view(), name='ServicesByConsultantView'),
    path('api/SalesByConsultant/', views.SalesByConsultantView.as_view(), name='SalesByConsultantView'),
    path('api/site_group_list/', views.site_group_list, name='site_group_list'),
    path('api/customeroutstanding/', views.CustomerOutstandingAPIView.as_view(), name='customeroutstanding'),
    path('api/currentuser/', views.CurrentUserAPIView.as_view(), name='currentuser'),
    path('api/about/', views.AboutListAPIView.as_view(), name='about'),
    path('api/confirmbooking/', views.ConfirmBookingApptView.as_view(), name='confirmbooking'),
    path('api/confirmbooking/<int:pk>/', views.ConfirmBookingApptView.as_view(), name='confirmbooking'),
    path('api/upload/', views.PdfSave.as_view(), name='upload'),
    path('api/getotp/', views.getTOTPAPIView.as_view(), name='getotp'),
    path('api/stripecheckoutview/', views.StripeCheckoutViewAPI.as_view(), name='stripecheckoutview'),
    path('api/testpayment', views.TestPaymentAPIView.as_view(), name='testpayment'),
    path('api/stripecustomercreate', views.StripeCustomerCreateAPIView.as_view(), name='stripecustomercreate'),
    path('api/stripepaymentintentcreate', views.StripePaymentIntentCreateAPIView.as_view(), name='stripepaymentintentcreate'),
    path('api/stripepaymentintentconfirm', views.StripePaymentIntentConfirmAPIView.as_view(), name='stripepaymentintentconfirm'),
    # path('api/securitylevellistpost', views.SecuritylevellistPostAPI.as_view(), name='securitylevellistpost'),
    path('api/schedulemonthappt/', views.ScheduleMonthAppointListAPIView.as_view(), name='schedulemonthappt'),
    # path('api/apptchannel/', views.ApptChannelAPIView.as_view(), name='apptchannel'),
    path('api/treatmentpackageinsert', views.TreatmentPackageInsertAPIView.as_view(), name='treatmentpackageinsert'),
    path('api/treatmentpackagelist', views.TreatmentPackageListAPIView.as_view(), name='treatmentpackagelist'),
    path('api/itemsitelistinitial/', views.ItemSitelistIntialAPIView.as_view(), name='itemsitelistinitial'),
    path('api/staffinsert/', views.StaffInsertAPIView.as_view(), name='staffinsert'),
    path('api/excelstaffinsert/', views.ExcelStaffInsertAPIView.as_view(), name='excelstaffinsert'),
    path('api/excelcustomerinsert/', views.ExcelCustomerInsertAPIView.as_view(), name='excelcustomerinsert'),
    path('api/fmspwuserlist/', views.FmspwListAPIView.as_view(), name='fmspwuserlist'),
    path('api/excelstockinsert/', views.ExcelStockInsertAPIView.as_view(), name='excelstockinsert'),
    path('api/tmptreatmentnewservice/', views.TmpTreatmentNewServiceAPIView.as_view(), name='tmptreatmentnewservice'),
    path('api/gender/', views.GenderListAPIView.as_view(), name='gender'),
    path('api/itemflexiservice/', views.ItemFlexiserviceListAPIView.as_view(), name='itemflexiservice'),
    path('api/staffperformance/', views.staffPerformanceAPIView.as_view(), name='staffperformance'),
    path('api/staffcustomerhistory/', views.staffCustomerHistoryAPIView.as_view(), name='staffcustomerhistory'),
    path('api/securitylevellistdupdel/', views.SecuritylevellistDuplicateDelete.as_view(), name='securitylevellistdupdel'),
    path('api/custsearchclass/', views.CustSearchClassAPI.as_view(), name='custsearchclass'),
    path('api/tmptreatmentnewservice/<int:pk>/', views.TmpTreatmentNewServiceAPIView.as_view(), name='tmptreatmentnewservice'),
    path('api/customerinvoicetemplateupload/', views.customerinvoicetemplateupload.as_view(), name='customerinvoicetemplateupload'),
    path('api/customerinvoicetemplatefiledownload/', views.customerinvoicetemplatefiledownload.as_view(), name='customerinvoicetemplatefiledownload'),
    path('api/prepaidvalidperiod/', views.PrepaidValidperiodAPIView.as_view(), name='prepaidvalidperiod'),
    path('api/customerreceiptprintbeforecheckout/', views.CustomerReceiptPrintBeforeCheckoutList.as_view(), name='customerreceiptprintbeforecheckout'),
    path('api/availableservicetimeslots/', views.AvailableTimeSlotsAPIView.as_view(), name='availableservicetimeslots'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)