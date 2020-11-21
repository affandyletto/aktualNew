from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from mutasi.models import mutasi,plt
from talenta.models import talenta
from pegawai.models import pegawai
from pensiun.models import pensiun
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def dashboard(request):
	if request.user.is_authenticated :
		pass
	else:
		return redirect('login')
	user 		=request.user
	mutate		=mutasi.objects.filter(terkirim=False)
	plte 		=plt.objects.filter(terkirim=False)
	talent 		=talenta.objects.filter(terkirim=False)
	pegg		=pegawai.objects.all()
	pensi 		=pensiun.objects.filter(terkirim=False)	
	mutateall	=mutasi.objects.all()
	plteall		=plt.objects.all()
	talentall	=talenta.objects.all()
	pensiall	=pensiun.objects.all()
	context	={
		'user':user,
		'mutate':mutate,		
		'mutateall':mutateall,
		'plte':plte,
		'plteall':plteall,
		'talent':talent,
		'talentall':talentall,
		'pegg':pegg,
		'pensi':pensi,
		'pensiall':pensiall

	}
	return render(request,'dashboard.html',context )

def loading(request):
	return render(request,"loading.html")

def loginView(request):
	context={
		'page_title':'LOGIN',
	}
	user=None

	if request.method=="GET":
		if request.user.is_authenticated:
			#logika untuk user
			return redirect('dashboard.html')
		else:
			#logika salah password
			return render(request,'login.html',context)

	if request.method == "POST":
		username_login=request.POST['username']
		password_login=request.POST['password']
		user=authenticate(request,username=username_login, password=password_login)
		if user is not None:
			login(request,user)
			return redirect('dashboard')
		else:
			return redirect('login')
	print(user)
	return render(request,'login.html',context)

def logoutView(request):
	logout(request)
	return redirect('login')
