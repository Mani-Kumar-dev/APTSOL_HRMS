from django.shortcuts import render,redirect
from AGT_admin_app.models import Employee_detail

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        current_user=request.user
        emps=Employee_detail.objects.get(Email=current_user.email)
        context={"emp":emps}
        return render(request,"index.html",context)
    else:
         return render(request,'login.html')
