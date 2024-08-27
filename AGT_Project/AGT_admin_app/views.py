from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import MultipleObjectsReturned
from AGT_admin_app.models import Employee_detail
from django.contrib import auth, messages
# Create your views here.
def admin_app(request):
    if request.user.is_authenticated:
        current_user=request.user
        emp=Employee_detail.objects.get(Email=current_user.email)
        context={"emp":emp}
        return render(request,"admin.html",context)
    else:
         return render(request,'login.html')

def allemps(request):
    if request.user.is_authenticated:
        emps=Employee_detail.objects.all()
        current_user=request.user
        emp=Employee_detail.objects.get(Email=current_user.email)
        context={
                 "emp":emp,
                 "emps":emps
                 }
        print(context)
        return render(request,"allempdetails.html",context)
    else:
         return render(request,'login.html')

def add_Hr(request):
    if request.user.is_authenticated:
        current_url  = request.build_absolute_uri()[-9:-1]
        context={"current_url":current_url }
        return render(request,"signin.html",context)
    else:
         return render(request,'login.html')

    
def add_admin(request):
    if request.user.is_authenticated:
        current_url  = request.build_absolute_uri()[-12:-1]
        context={"current_url":current_url }
        return render(request,"signin.html",context)
    else:
         return render(request,'login.html')

def emp_signin(request):
    if request.user.is_authenticated:
        current_url = request.build_absolute_uri()[-10:-1]
        context={"current_url":current_url }
        return render(request,"signin.html",context)
    else:
         return render(request,'login.html')
def remove_employee(request, Emp_Id):
    if request.user.is_authenticated:
        if  Emp_Id:
            try:  
                emp_to_be_removed =get_object_or_404(Employee_detail, Emp_Id= Emp_Id)
                emp_to_be_removed.delete()
                messages.success(request, 'Employee successfully deleted.')
                return redirect("/allemps")
            except:
                messages.error(request, 'Failed to delete employee.')
                return redirect("/allemps/")
            return render(request, 'remove.html')
    else:
        return render(request,'login.html')

def editemp(request, Emp_Id):
    if request.user.is_authenticated:
        try:
            emps = Employee_detail.objects.get(Emp_Id=Emp_Id)
            context = {"emps": emps, "emp": emps }

            if request.method == "POST":
                if 'Emp_Id' in request.POST:
                    employee = get_object_or_404(Employee_detail, pk=Emp_Id)
                    employee.image=request.FILES.get("image")
                    employee.First_Name=request.POST.get("First_Name")
                    employee.Last_Name=request.POST.get("Last_Name")
                    employee.Email=request.POST.get("Email")
                    employee.Contact=request.POST.get("Contact")
                    employee.Department=request.POST.get("Department")
                    employee.Designation=request.POST.get("Designation")
                    employee.Salary=request.POST.get("Salary")
                    employee.BasicPay=request.POST.get("BasicPay")
                    employee.PAN=request.POST.get("PAN")
                    employee.UAN=request.POST.get("UAN")
                    employee.BankAccount=request.POST.get("Bankaccount")
                    employee.Location=request.POST.get("Location")
                    
                    employee.save()
                    messages.success(request, "Successfully Updated")
                    return redirect("/allemps")
                else:
                    messages.error(request, "Invalid form submission")
                    return render(request, "editemp.html", context) 
            elif request.method == "GET":
                return render(request, "editemp.html", context) 
            else:
                messages.error(request, "Unsupported request method")
                return render(request, "editemp.html", context) 

        except Exception as e:
            messages.error(request, f"Error retrieving/updating employee: {e}")
            return render(request, "editemp.html", context)  

    else:
        return render(request, 'login.html')
    

