
from django.urls import path
from .import views

urlpatterns = [
  path('signin/',views.signin,name="signin"),
  path('',views.loginform,name="login"),
  path('logout/',views.handlelogout,name="logout")
  

]