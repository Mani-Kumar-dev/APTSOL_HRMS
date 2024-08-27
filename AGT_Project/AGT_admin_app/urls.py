
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AGT_admin_app import views

urlpatterns = [
   path("admin_app/",views.admin_app,name="admin_app"),
   path("allemps/",views.allemps,name="allemps"),
   path("hrsignin/",views.add_Hr,name="hrsignin"),
   path("adminsignin/",views.add_admin,name="adminsignin"),
   path('Empsignin/',views.emp_signin,name="Empsignin"),
   path('confirm_delete/<slug:Emp_Id>/', views.remove_employee, name='confirm_delete'),
   path('edit_emp/<slug:Emp_Id>/',views.editemp,name="edit_emp"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)