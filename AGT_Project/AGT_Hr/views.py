from django.shortcuts import render,redirect
from django.contrib import messages
from AGT_admin_app.models import Employee_detail,Depart
from AGT_admin_app.models import LeaveRequest,Payslip
from django.db import IntegrityError
#sending email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def Hr_manage(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emp":emps}
        return render(request,"Hr_Manage.html",context)
    else:
         return render(request,'login.html')

def AddEmps(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emp":emps}
        if request.method == "POST":
            image=request.FILES.get("image")
            First_Name=request.POST.get("First_Name")
            Last_Name=request.POST.get("Last_Name")
            Email=request.POST.get("Email")
            Contact=request.POST.get("Contact")
            Emp_Id=request.POST.get("Emp_Id")
            Department=request.POST.get("Department")
            Designation=request.POST.get("Designation")
            Salary=request.POST.get("Salary")
            BasicPay=request.POST.get("BasicPay")
            PAN=request.POST.get("PAN")
            UAN=request.POST.get("UAN")
            BankAccount=request.POST.get("Bankaccount")
            Location=request.POST.get("Location")
            department,Created= Depart.objects.get_or_create(name=Department)
            query=Employee_detail(image=image,First_Name=First_Name,Last_Name=Last_Name,Email=Email,Contact=Contact,Emp_Id=Emp_Id,Department=department,Designation=Designation,Salary=Salary,BasicPay=BasicPay,PAN=PAN,UAN=UAN,BankAccount=BankAccount,Location=Location)
            query.save()
            messages.success(request,"Successfully Added")
            return redirect("/allemps")
        elif request.method == "GET":
            return render(request,"add_emps.html",context)
        else:
            messages.error(request,"Unsuccessfull")
            return redirect("/AddEmps")
    else:
         return render(request,'login.html')

    

def ID_Card(request,Emp_Id):
    if request.user.is_authenticated:
        emps=Employee_detail.objects.get(Emp_Id=Emp_Id)
        context={"emps":emps,
                "emp":emps
                }
        return render(request,"agt_Id.html",context)
    else:
        return render(request,'login.html')
def Emp_info(request,Emp_Id):
    if request.user.is_authenticated:
        emps=Employee_detail.objects.get(Emp_Id=Emp_Id)
        context={"emps":emps,
                 "emp":emps
                }
        return render(request,"emp_info.html",context)
    else:
        return render(request,'login.html')
def Handle_leave_requests(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        leaverequests=LeaveRequest.objects.all()
        context={"emp":emps,"leaverequests":leaverequests}
        return render(request,"leavesemp.html",context)
    else:
         return render(request,'login.html')
def accept_leave_request(request, leaves_id):
    if request.user.is_authenticated:
        try:
            leave_request = LeaveRequest.objects.get(id=leaves_id)
        except LeaveRequest.DoesNotExist:
            messages.error(request, "Leave request not found.")
            return redirect("/handleleaves/")
        leave_request.status = 'Accepted'
        leave_request.save()
        
        # Send emails
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_admin = mail.EmailMessage(
            'Leave Request Accepted',
            f'The leave request from {leave_request.start_date} {leave_request.end_date} has been Approved.\n\nBest Regards From HR\nAptsol Global Tech Pvt Ltd.',
            from_email,
            [leave_request.Emp_Id.Email],
            connection=connection
        )
        connection.send_messages([email_admin])
        connection.close()

        messages.success(request, "Leave request accepted successfully.")
        return redirect("/handleleaves/")
    else:
       
        return render(request, "login.html")



def reject_leave_request(request, leaves_id):
    if  request.user.is_authenticated:
        leave_request = LeaveRequest.objects.get(id=leaves_id)
        if leave_request:
            leave_request.status = 'Rejected'
            leave_request.save()
            # Send emails
            from_email = settings.EMAIL_HOST_USER
            connection = mail.get_connection()
            connection.open()
            email_admin = mail.EmailMessage(
            'Leave Request Accepted',
            f'The leave request from {leave_request.start_date} {leave_request.end_date} has been Rejected.\n\nBest Regards From HR\nAptsol Global Tech Pvt Ltd.',
            from_email,
            [leave_request.Emp_Id.Email],
            connection=connection
            )
            connection.send_messages([email_admin])
            connection.close()
            messages.success(request, "Leave request Rejected Successfully.")
            return redirect("/handleleaves/")
        else:
            messages.error(request, "Leave request not found.")
            return redirect("/handleleaves/")
    else:
        return render(request, "login.html")
    

def addpayslips(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emps,"emp":emps,}
        return render(request,"addpayslips.html",context)
    else:
         return render(request,'login.html')


def accept_leave_request(request, leaves_id):
    if request.user.is_authenticated:
        try:
            leave_request = LeaveRequest.objects.get(id=leaves_id)
        except LeaveRequest.DoesNotExist:
            messages.error(request, "Leave request not found.")
            return redirect("/handleleaves/")
        leave_request.status = 'Accepted'
        leave_request.save()
        
        # Send emails
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_admin = mail.EmailMessage(
            'Leave Request Accepted',
            f'The leave request from {leave_request.start_date} {leave_request.end_date} has been Approved.\n\nBest Regards From HR\nAptsol Global Tech Pvt Ltd.',
            from_email,
            [leave_request.Emp_Id.Email],
            connection=connection
        )
        connection.send_messages([email_admin])
        connection.close()

        messages.success(request, "Leave request accepted successfully.")
        return redirect("/handleleaves/")
    else:
        return render(request, "login.html")
   
def create_Payslips(request,Emp_Id):
    if request.user.is_authenticated:
        current_user=request.user
        emp=Employee_detail.objects.get(Emp_Id=Emp_Id)
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emps":emp,"emp":emps}
        if request.method == "POST":
            payslip_pdf=request.FILES.get("Payslip")
            # Emp_Id=request.POST.get("Emp_Id")
            month=request.POST.get("Month")
            try:
                query=Payslip(Emp_Id=emp,month=month,payslip_pdf=payslip_pdf)
                query.save()
                messages.success(request,"Successfully Added")
                # Send emails
                from_email = settings.EMAIL_HOST_USER
                connection = mail.get_connection()
                connection.open()
                leave_link = 'http://127.0.0.1:8000/payslips/'  # Replace with the actual URL
                email_content = (
                    f'The payslips for the month {month} has been updated.You can view the details <a href="{leave_link}">here</a>.<p>Best Regards From HR<br>Aptsol Global Tech Pvt Ltd.</p>'
                )

                email_admin = mail.EmailMessage(
                'Payslips  Uploaded',
                email_content,
                from_email,
                [emp.Email],
                connection=connection,
                )
                email_admin.content_subtype = "html"  # Set content type to HTML
                email_admin.send()

                connection.close()
                return redirect("/allemps")
            except IntegrityError as e:
                print("Error saving object:", e)
            except Exception as e:
                print("An unexpected error occurred:", e)

        elif request.method == "GET":
            return render(request,"addpayslips.html",context)
        else:
            messages.error(request,"Unsuccessfull")
            return redirect("/AddEmps")
    else:
         return render(request,'login.html')
    
def allpdfs(request,Emp_Id):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        employee=Employee_detail.objects.get(Emp_Id=Emp_Id)
        context={"emps":emps,"emp":emps,"employee":employee}
        return render(request,"allpdfs.html",context)
    else:
         return render(request,'login.html')