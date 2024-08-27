from django.contrib import admin
from AGT_admin_app.models import Employee_detail,Depart,LeaveType,LeaveRequest,Payslip

admin.site.register(Employee_detail)
admin.site.register(Depart)
admin.site.register(LeaveType)
admin.site.register(LeaveRequest)
admin.site.register(Payslip)