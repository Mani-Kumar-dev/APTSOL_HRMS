from django.shortcuts import render,get_object_or_404,redirect
from django.http import FileResponse
import mimetypes
from django.contrib import messages
from AGT_admin_app.models import Employee_detail,LeaveRequest,LeaveType,Payslip
import calendar
from datetime import datetime, timedelta

# Create your views here.
def Employee_Info(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,"emp":emps,}
        return render(request,"Employee.html",context)
    else:
         return render(request,'login.html')

def LMS(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,"emp":emps,}
        return render(request,"Lms.html",context)
    else:
        return render(request,"login.html")
def leave_request(request,Emp_Id):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,
                 "emp":emps,
                }
        if request.method == "POST":
            start_date=request.POST.get("start_date")
            end_date=request.POST.get("end_date")
            reason=request.POST.get("reason")
            leave_type=request.POST.get("leavetype")
            leave_type,Created= LeaveType.objects.get_or_create(name=leave_type)
            query=LeaveRequest.objects.create(Emp_Id=emps,start_date=start_date,end_date=end_date,reason=reason,leave_type=leave_type,status='Pending')
            query.save()
            messages.success(request,"Request Done")
            return redirect("/leavestatus/"+emps.Emp_Id)
        elif request.method == "GET":
            return render(request,"leaverequest.html",context)
        else:
            messages.error(request,"Unsuccessfull")
            return redirect("/leaverequest/"+emps.Emp_Id)
    else:
        return render(request,"login.html")

def leavestatus(request,Emp_Id):
    if request.user.is_authenticated:
        emps=Employee_detail.objects.get(Emp_Id=Emp_Id)
        leaverequest=LeaveRequest.objects.filter(Emp_Id=emps)
      
        context={"emps":emps,
                 "emp":emps,
                 "leaverequest":leaverequest,
                 }
        return render(request,"leavestatus.html",context)
    else:
        return render(request,"login.html")
def mypayrolls(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,
                 "emp":emps,
                }
        return render(request,"payrolls.html",context)
    else:
        return render(request,"login.html")

def payslips(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        payslips=Payslip.objects.filter(Emp_Id=emps)
        context={"emps":emps,
                 "emp":emps,
                 "payslips":payslips
                }
        return render(request,"payslips.html",context)
    else:
        return render(request,"login.html")
def myhr(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,"emp":emps,}
        return render(request,"myhr.html",context)
    else:
         return render(request,'login.html')
      
def download_pdf(request, month):
    current_user=request.user
    emps=Employee_detail.objects.get(Email=current_user.email)
    obj = get_object_or_404(Payslip,Emp_Id=emps,month=month)
    file_type, file_encoding = mimetypes.guess_type(obj.payslip_pdf.name)

    if obj.payslip_pdf:
        response = FileResponse(obj.payslip_pdf, content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename="{obj.payslip_pdf.name.split("/")[-1]}"'
        return response