from django.shortcuts import render, redirect
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView
from .models import pegawai
from mutasi.models import mutasi,plt
from talenta.models import talenta
from pensiun.models import pensiun
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.template.loader import get_template
import datetime
from .forms import pegawaiForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(redirect_field_name='login')
def hapusPegawai(request,*args,**kwargs):
	if request.method =='POST':
		fruits = request.POST.getlist('cek')
		cekHapus=0
		for mu in fruits:
			try:
				pegg=pegawai.objects.get(nipeg=mu)
			except:
				pass

			try:
				mut=mutasi.objecs.get(peg=pegg).peg = None
				mut.save()
			except:
				pass

			try:
				pl=plt.objecs.get(peg=pegg).peg = None
				pl.save()
			except:
				pass

			try:
				talen=talenta.objecs.get(peg=pegg).peg = None
				talen.save()
			except:
				pass
				
			try:
				pensi=pensiun.objecs.get(peg=pegg).peg = None
				pensi.save()
			except:
				pass

			try:			
				pegg.delete()
				cekHapus+=1
			except:
				pass

		if cekHapus>0:
			messages.success(request, 'anda telah menghapus '+ str(cekHapus)+' data pegawai')

	return redirect('pegawai:index')

class pegawaiView(LoginRequiredMixin,ListView):
	template_name ='pegawai/index.html'
	queryset 	  = pegawai.objects.all()
	redirect_field_name = 'pegawai/index.html'
	login_url 			= '/login/'

class pegawaiUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = pegawai
	form_class = pegawaiForm	
	template_name = "pegawai/edit.html"
	success_url 	= '..'
	redirect_field_name = 'pegawai/index.html'
	login_url 			= '/login/'
	success_message = 'Anda berhasil meng Update data pegawai'

@login_required(redirect_field_name='login')
def delete(request,*args,**kwargs):
	pegawai_delete=pegawai.objects.get(id=kwargs["pk"])
	nipeg=pegawai_delete.nipeg
	pegawai_delete.delete()
	messages.success(request, 'pegawai dengan nipeg : '+ str(nipeg)+' telah di hapus')
	return redirect('pegawai:index')

class pegawaiCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
	form_class = pegawaiForm
	template_name = 'pegawai/edit.html'
	success_url 	= '..'
	redirect_field_name = 'pegawai/index.html'
	login_url 			= '/login/'
	success_message = 'Anda berhasil menambah data pegawai'
	success_url 	= '..'

def tambah(request):
	if request.method =="POST":
		no=request.POST['no']
		nipeg=request.POST['nipeg']
		nama=request.POST['nama']
		unit=request.POST['unit']
		email=request.POST['email']
		noHp=request.POST['noHp']
		try :
			pegawai.objects.get(nipeg=nipeg)			
			return redirect('pegawai:tambah')
		except:
			tambahPegawai = pegawai.objects.create(no=no,nipeg=nipeg,nama=nama,unit=unit,email=email,noHp=noHp)
			tambahPegawai.save()	
			return redirect('pegawai:index')
		

	context={}

	return render(request,'pegawai/tambah.html',context)