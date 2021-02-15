

#menu/urls.py
from django.urls import path

from . import views



urlpatterns = [
	#localhost:8000
	#empty or blank URL

    path('', views.clientsListing, name = 'clientsList'),


]