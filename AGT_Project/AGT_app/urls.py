
from django.urls import path
from AGT_app import views

urlpatterns = [
   path('home/',views.home,name="home"),
]