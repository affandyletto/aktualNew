from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,UpdateView
from .models import talenta,kriteriaTalenta,tglKriteria,PhDP
from pegawai.models import pegawai
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail,EmailMessage
from wkhtmltopdf.views import PDFTemplateView,PDFTemplateResponse
from django.template.loader import get_template
import datetime
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin

class talentaView(ListView):
	template_name ='talenta/index.html'
	queryset 	  = talenta.objects.all()

class PhDPView(ListView):
	template_name ='talenta/PhDP.html'
	try:
		queryset 	  = PhDP.objects.all()
	except:
		pass

class kriteriaTalentaView(ListView):
	template_name ='talenta/kriteria.html'
	context_object_name = 'talent'
	def get_queryset(self):
		try:
			queryset = {'talenta': kriteriaTalenta.objects.all(), 'tgl': tglKriteria.objects.get(posisi="akhir"),'tglA': tglKriteria.objects.get(posisi="awal")}
		except:
			try:
				queryset = {'talenta': kriteriaTalenta.objects.all()}
			except:
				pass
		return queryset

class talentaUpdate(SuccessMessageMixin,UpdateView):
	model = talenta
	form_class = talentaForm	
	template_name 	= "talenta/edit.html"
	success_url 	= '..'
	success_message = 'Anda berhasil meng Update Talenta'

class kriteriaUpdate(SuccessMessageMixin,UpdateView):
	model = kriteriaTalenta
	form_class = kriteriaForm	
	template_name 	= "talenta/edit.html"
	success_url 	= '../../talenta/kriteria'
	success_message = 'Anda berhasil meng Update Kriteria Talenta'

class phdpUpdate(SuccessMessageMixin,UpdateView):
	model = PhDP
	form_class = PhDPForm	
	template_name 	= "talenta/edit.html"
	success_url 	= '../../talenta/PhDP'
	success_message = 'Anda berhasil meng Update PHDP'

def delete(request,*args,**kwargs):
	talenta_delete=talenta.objects.get(id=kwargs["pk"])
	talenta_delete.delete()
	return redirect('talenta:index')

def kriteriaDelete(request,*args,**kwargs):
	talenta_delete=kriteriaTalenta.objects.get(id=kwargs["pk"])
	talenta_delete.delete()
	return redirect('talenta:kriteria')

def phdpDelete(request,*args,**kwargs):
	phdp_delete=PhDP.objects.get(id=kwargs["pk"])
	phdp_delete.delete()
	return redirect('talenta:PhDP')

class PDFTemplateView(DetailView):
	model= talenta
	template_name='talenta/pdf_talenta.html'
	context={}
	
	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()
		self.template = get_template(self.template_name)
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}
		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="render_talenta.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,}
									 )
		
		return response

class PDFPhDP(DetailView):
	model= PhDP
	template_name='talenta/pdf_PhDP.html'
	context={}
	
	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()
		self.template = get_template(self.template_name)
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}
		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="PhDP.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,}
									 )
		
		return response

class PDFKriteria(DetailView):
	model= kriteriaTalenta
	template_name='talenta/pdf_kriteriaTalenta.html'
	context={}
	
	def get(self,request,*args,**kwargs):
		self.context['sesuatu']=self.get_object()
		self.context['tglAwal']=tglKriteria.objects.get(posisi="awal")
		self.context['tglAkhir']=tglKriteria.objects.get(posisi="akhir")
		self.template = get_template(self.template_name)
		options ={
			'page-size': 'Letter',
			'encoding': "UTF-8",
		}		

		response=PDFTemplateResponse(request=request,
									 template=self.template,
									 filename ="kriteriaTalenta.pdf",
									 context=self.context,
									 show_content_in_browser=True,
									 cmd_options={'margin-top': 0,}
									 )
		
		return response
