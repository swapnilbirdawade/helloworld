from django.shortcuts import render
# from django.template import Context
from .models import Drivers
from django.http import HttpResponse
# Create your views here.
def clientsListing(request):

	#logic to retrive the data from the database and show it in clients.html
	#context = {"client_page":"active"}
	# clientlistings =Drivers.objects.all().filter(is_exp=True)
	clientlistings =Drivers.objects.all()
	print("Recieved drivers Records",len(clientlistings))
	context = {
			'driverList' :clientlistings ,
			'name':'Swapnil',
			'client_page':'active'
	}

	return render(request,'clients/clients.html',context)

