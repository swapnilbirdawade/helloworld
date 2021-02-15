
#menu/urls.py
from django.urls import path

from . import views



urlpatterns = [
	#localhost:8000
	#empty or blank URL

    path('home/', views.homemenu, name = 'myhome'),
    path('about/', views.aboutmenu, name = 'myabout'),
    path('', views.loginmenu, name = 'mylogin'),
    path('register/', views.registermenu, name = 'myregister'),
    path('logout/', views.logoutmenu, name = 'mylogout'),


]