
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import SignInForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password != confirm_password:
                messages.info(request, "Passwords do not match")
                return redirect('/signin')
            
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/signin')

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('/signin')

            try:
                previous_url = request.META.get('HTTP_REFERER')
                if previous_url[-9:-1]=="hrsignin":
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.is_staff = True
                    user.save()
                elif previous_url[-12:-1]=="adminsignin":
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.is_staff = True
                    user.is_superuser =True
                    user.save()
                elif previous_url[-10:-1] == "Empsignin":
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.is_active = True
                    user.save()
                    
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                messages.info(request, "Successfully signed up")
                return redirect('/')  
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('/signin')
        else:
            messages.error(request, "Invalid form data")
            return redirect('/signin')
    else:
        form = SignInForm()
    
    return render(request, 'signin.html', {'form': form})



def loginform(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/login')
        else:
            messages.error(request, "Invalid form data")
            return redirect('/login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('/')