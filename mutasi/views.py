from django.shortcuts import render, redirect
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView
from django.core import mail
from django.core.mail import send_mail,EmailMessage
from .models import mutasi,plt,aps
from talenta.models import talenta
from pegawai.models import pegawai
from django.http import HttpResponseRedirect, HttpResponse
from wkhtmltopdf.views import PDFTemplateView,PDFTemplateResponse
from django.template.loader import get_template
from .forms import mutasiForm,pltForm,apsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import datetime
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from django_endesive import pdf
from endesive.pdf import fpdf
from endesive.pdf import cms
from django.core.files import File
import requests
import json

class mutasiView(LoginRequiredMixin,ListView):
	template_name		='mutasi/index.html'
	queryset 	  		= mutasi.objects.all()
	pegNone				=mutasi.objects.filter(peg=None)
	redirect_field_name = 'mutasi/index.html'
	login_url 			= '/login/'
	extra_context 		= {
		'pegNone':pegNone,
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class apsView(LoginRequiredMixin,ListView):
	template_name		='mutasi/aps.html'
	queryset 	  		= aps.objects.all()
	pegNone				= aps.objects.filter(peg=None)
	redirect_field_name = 'mutasi/aps.html'
	login_url 			= '/login/'
	extra_context 		= {
		'pegNone':pegNone,
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)


class pltView(LoginRequiredMixin,ListView):
	template_name ='mutasi/plt.html'
	queryset 	  = plt.objects.all()
	pegNone=plt.objects.filter(peg=None)
	redirect_field_name = 'mutasi/plt.html'
	login_url 			= '/login/'
	extra_context = {
		'pegNone':pegNone,
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class mutasiCreate(LoginRequiredMixin,SuccessMessageMixin, CreateView):
	form_class = mutasiForm
	template_name = 'mutasi/edit.html'
	success_message = 'Anda berhasil membuat Mutasi'
	success_url 	= '..'

	redirect_field_name = 'mutasi/index.html'
	login_url 			= '/login/'

	extra_context = {
		'page_title':'SK Mutasi Jabatan',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class apsCreate(LoginRequiredMixin,SuccessMessageMixin, CreateView):
	form_class = apsForm
	template_name = 'mutasi/edit.html'
	success_url 	= 'aps'
	success_message = 'Anda berhasil membuat APS'

	redirect_field_name = 'mutasi/aps.html'
	login_url 			= '/login/'

	extra_context = {
		'page_title':'Surat Keputusan APS',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class pltCreate(LoginRequiredMixin,SuccessMessageMixin, CreateView):
	form_class = pltForm
	template_name = 'mutasi/edit.html'
	success_url 	= 'plt'
	success_message = 'Anda berhasil membuat PLT'

	redirect_field_name = 'mutasi/plt.html'
	login_url 			= '/login/'

	extra_context = {
		'page_title':'Surat Penugasan PLT',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class mutasiUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = mutasi
	form_class = mutasiForm
	template_name = "mutasi/edit.html"
	success_url 	= '..'
	success_message = 'Anda berhasil meng Update mutasi'

	redirect_field_name = 'mutasi/index.html'
	login_url 			= '/login/'

	extra_context = {
		'page_title':'SK Mutasi Jabatan',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class apsUpdate(LoginRequiredMixin,SuccessMessageMixin, UpdateView):

	model = aps
	form_class = apsForm
	
	template_name = "mutasi/edit_aps.html"
	success_url 	= '../aps'
	success_message = 'Anda berhasil meng Update aps'

	redirect_field_name = 'mutasi/aps.html'
	login_url 			= '/login/'
	extra_context = {
		'page_title':'Surat Keputusan APS',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class pltUpdate(LoginRequiredMixin,SuccessMessageMixin, UpdateView):

	model = plt
	form_class = pltForm
	
	template_name = "mutasi/edit_plt.html"
	success_url 	= '../plt'
	success_message = 'Anda berhasil meng Update plt'

	redirect_field_name = 'mutasi/plt.html'
	login_url 			= '/login/'
	extra_context = {
		'page_title':'Surat Penugasan PLT',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

@login_required(redirect_field_name='login')
def delete(request,*args,**kwargs):
	mutasi_delete=mutasi.objects.get(id=kwargs["pk"])
	nipeg=mutasi_delete.nipeg
	mutasi_delete.delete()	
	messages.success(request, 'Mutasi dengan nipeg :'+ str(nipeg)+' telah di hapus')
	return redirect('mutasi:index')

@login_required(redirect_field_name='login')
def deletePLT(request,*args,**kwargs):
	mutasi_delete=plt.objects.get(id=kwargs["pk"])
	nipeg=mutasi_delete.nipeg
	mutasi_delete.delete()	
	messages.success(request, 'PLT dengan nipeg :'+ str(nipeg)+' telah di hapus')
	return redirect('mutasi:plt')

@login_required(redirect_field_name='login')
def deleteAPS(request,*args,**kwargs):
	mutasi_delete=aps.objects.get(id=kwargs["pk"])
	nipeg=mutasi_delete.nipeg
	mutasi_delete.delete()	
	messages.success(request, 'APS dengan nipeg :'+ str(nipeg)+' telah di hapus')
	return redirect('mutasi:aps')

class pdf_mutasi(LoginRequiredMixin,DetailView):
	model= mutasi
	template='mutasi/pdf_mutasi.html'
	context={}
	
	redirect_field_name = 'mutasi/index.html'
	login_url 			= '/login/'

	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()		
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}	
		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="mutasi.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,

									 }
									 )

		return response

class pdf_plt(LoginRequiredMixin,DetailView):
	model= plt
	template='mutasi/pdf_plt.html'
	context={}

	redirect_field_name = 'mutasi/plt.html'
	login_url 			= '/login/'

	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()		
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}
		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="plt.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,}
									 )
		
		return response

class pdf_aps(LoginRequiredMixin,DetailView):
	model= aps
	template='mutasi/pdf_aps.html'
	context={}

	redirect_field_name = 'mutasi/aps.html'
	login_url 			= '/login/'

	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()		
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}
		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="aps.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,}
									 )
		
		return response