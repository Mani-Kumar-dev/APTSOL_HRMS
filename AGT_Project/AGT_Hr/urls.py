
from django.urls import path
from AGT_Hr import views

urlpatterns = [
   path('Hr_manage/',views.Hr_manage,name="Hr_manage"),
   path('AddEmps/',views.AddEmps,name="AddEmps"),
   path('Id_card/<slug:Emp_Id>/',views.ID_Card,name="Id_card"),
   path('Emp_info/<slug:Emp_Id>/',views.Emp_info,name="Emp_info"),
   path('handleleaves/',views.Handle_leave_requests,name="handleleaves"),
   path('accept_leave/<slug:leaves_id>/',views.accept_leave_request,name="accept_leave"),
   path('reject_leave/<slug:leaves_id>/',views.reject_leave_request,name="reject_leave"),
   path('createPayslips/<slug:Emp_Id>',views.create_Payslips,name="createPayslips"),
   path('allpdfs/<slug:Emp_Id>/',views.allpdfs,name="allpdfs"),
   
   
]