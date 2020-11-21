from django.shortcuts import render, redirect
from django.views.generic import ListView,RedirectView,DetailView,UpdateView
from .models import pensiun
from pegawai.models import pegawai
from general.wa import whatsapp_login,send_message_to_unsavaed_contact,send_attachment_to_unsavaed_contact
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.core import mail
from django.template.loader import get_template
from .forms import pensiunForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class pensiunView(LoginRequiredMixin,ListView):
	template_name ='pensiun/index.html'
	queryset 	  = pensiun.objects.all()
	login_url 			= '/login/'

class pensiunUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	model = pensiun
	form_class = pensiunForm
	
	template_name = "pensiun/edit.html"
	success_url 	= '..'
	redirect_field_name = 'pensiun/index.html'
	login_url 			= '/login/'
	success_message = 'Anda berhasil meng Update data pensiun'
	
@login_required(redirect_field_name='login')
def delete(request,*args,**kwargs):
	pensiun_delete=pensiun.objects.get(id=kwargs["pk"])
	nipeg=pensiun_delete.nipeg
	pensiun_delete.delete()
	messages.success(request, 'Pensiun dengan nipeg : '+ str(nipeg)+' telah di hapus')
	return redirect('pensiun:index')

@login_required(redirect_field_name='login')
def kirim(request,*args,**kwargs):

	if request.method =='POST':
		fruits = request.POST.getlist('cek')		
		pesanH=0
		mode=""
		if "hapus" in request.POST:			
			for mu in fruits:
				try :
					mutate = pensiun.objects.get(nipeg=mu)
					mutate.delete()
					pesanH+=1
				except:
					return redirect('pensiun:index')

			if pesanH>0:
				messages.success(request, 'Sebanyak '+ str(pesanH)+' SK telah dihapus')
		else:
			if 'kirimWa' in request.POST:
				whatsapp_login()
				mode="wa"
			pesanW=0
			pesanE=0
			connection = mail.get_connection()
			connection.open()
			for mu in fruits:				
				try : 
					mutate = pensiun.objects.get(nipeg=mu)
				except:
					return redirect('pensiun:index')

				file="C:/pln3"+mutate.file.url					
				if ('kirim' in request.POST or mutate.terkirim == False) and mutate.peg.email :
					message=EmailMessage("SK Pensiun "+mutate.peg.nipeg,
								"Yth. Bapak/Ibu "+mutate.peg.nama+"\nPegawai PT PLN (Persero) Unit Induk Distribusi Jawa Timur \n\nTerlampir disampaikan Surat Keputusan pensiun atas nama bapak/ibu "+mutate.peg.nama+", Jika \nmenemukan perbedaan silahkan menghubungi pengelola SDM Unit setempat.\n\nEmail ini dikirim melalui sistem e-statement otomatis, mohon untuk tidak membalas. \n\nDemikian dan atas perhatian Bapak/Ibu dihaturkan terima kasih. \n\n\n\nSalam, \n\nTim AKTUAL \nBidang SDM \nPT PLN (Persero) UID Jawa Timur \n",
								"SDM",[mutate.peg.email],connection=connection)
					message.attach_file(file)
					message.send()	
					mutate.terkirim = True
					mutate.save()
					pesanE+=1

				if mode=="wa" and mutate.peg.noHp:											
					send_message_to_unsavaed_contact(mutate.peg.noHp,"SK Pensiun anda telah dikirim pada Email : " + mutate.peg.email,1)			
					pesanW+=1	
			
			if pesanE>0:
				messages.success(request, 'Pesan Email telah terkirim ke '+ str(pesanE)+' pegawai')
			elif pesanW>0:
				messages.success(request, 'Pesan WA telah terkirim ke'+ str(pesanW)+' pegawai')

			connection.close()
			
	return redirect('pensiun:index')

@login_required(redirect_field_name='login')
def tambah(request):
	if request.method =="POST":
		nipeg=request.POST['nipeg']
		file=request.FILES['file']
		try :
			pensiun.objects.get(nipeg=nipeg)	
			messages.success(request, 'Data pensiun dengan nipeg tersebut sudah ada')		
			return redirect('pensiun:tambah')
		except:
			tambahPensiun = pensiun.objects.create(nipeg=nipeg,file=file,terkirim=False,peg=None)
			tambahPensiun.save()
			messages.success(request, 'Berhasil menambahkan SK pensiun dengan nipeg '+ str(nipeg))
			return redirect('pensiun:index')	

	context={}

	return render(request,'pensiun/tambah.html',context)