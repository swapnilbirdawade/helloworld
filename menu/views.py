from django.shortcuts import render,redirect
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

def homemenu(request):
	context = {"home_page":"active"}
	return render(request,'menu/home.html',context)

def aboutmenu(request):
	context = {"about_page":"active"}
	return render(request,'menu/about.html',context)

def loginmenu(request):
	context = {"login_page":"active"}
	if request.method == 'POST':

		username=request.POST['username']
		password = request.POST['psw']

		user = auth.authenticate(username = username,password = password)

		if user is not None:
			auth.login(request,user)
			print("You are logged in")
			# messages.success(request,"You are now Logged in")

			return redirect("myhome")
		else:

			print("invalid Username/Password")
			messages.error(request,"Invalid username/password")

			return redirect("mylogin")
				


	else:
		return render(request,'menu/login.html',context)
			


	
def registermenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Logic to register the User
    # if request is GET then display the registration form
    # else if its POST request then process the Form - validate the user info and perform the action
    context = {"register_page": "active"}
    if request.method == 'POST':
    	print("I am in POST request")
    	username=request.POST['username']
    	email=request.POST['email']
    	password1=request.POST['psw']
    	password2=request.POST['psw-repeat']
    	print("username :",username)
    	print("email :",email)
    	print("password1 :",password1)
    	print("password2 :",password2)

    	if(password1==password2):
    		if User.objects.filter(username=username).exists():
    			print('The username is not available/its already exists')
    			messages.error(request,"The username is not available/its already exists")
    			return redirect('register')
    		else:
    			user = User.objects.create_user(username=username,password=password1,email=email)
    			user.save()
    			print("You are now registered and can login")
    			return redirect('mylogin')
    	else:
    		# print('Password do not match,please enter again')
    		messages.error(request,"Password do not match,please enter again")
    		return redirect("myregister")
    else:
    	print("I am in GET request")
    	return render(request,'menu/register.html',context)


def logoutmenu(request):
	# context = {"logout_page":"active"}
	print("You are logged out")
	auth.logout(request)
	return redirect('mylogin')






# def homemenu(request):
# 	# print("in homemenu")
# 	context = {"home_page": "active"}
# 	return render(request,'menu/home.html',context)


# def aboutmenu(request):

# 	context = {"about_page": "active"}
#  	# return render(request,'menu/about.html',context)
#  	return render(request, 'menu/about.html',context)

# def loginmenu(request):

# 	context = {"login_page": "active"}
#  	return render(request,'menu/login.html',context)

# def registermenu(request):

# 	context = {"register_page": "active"}
# 	return render(request,'menu/register.html',context) 	













