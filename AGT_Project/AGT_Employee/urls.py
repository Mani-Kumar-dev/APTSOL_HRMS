
from django.urls import path
from AGT_Employee import views

urlpatterns = [
  path("Employee_info/",views.Employee_Info,name="Employee_info"),
   path("lms/",views.LMS,name="lms"),
   path("leaverequest/<slug:Emp_Id>/",views.leave_request,name="leaverequest"),
   path("leavestatus/<slug:Emp_Id>/",views.leavestatus,name="leavestatus"),
   path("payrolls/",views.mypayrolls,name="payrolls"),
   path('payslips/',views.payslips,name="payslips"),
   path('myhr/',views.myhr,name="myhr"),
   path('download/<slug:month>/',views.download_pdf, name='download_pdf'),
   
]