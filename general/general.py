from django.shortcuts import render, redirect
from django.core import mail
from mutasi.models import mutasi,plt,aps
from talenta.models import talenta,kriteriaTalenta,tglKriteria,PhDP
from pegawai.models import pegawai
from pensiun.models import pensiun
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail,EmailMessage
from wkhtmltopdf.views import PDFTemplateView,PDFTemplateResponse
from .wa import *
import os
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.auth.models import User
from django_endesive import pdf
from endesive.pdf import fpdf
import datetime
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from endesive.pdf import cms
from django.core.files import File
import shutil
import json
import requests
import redis
import websocket
import random,time

def listToString(s):  
    
    # initialize an empty string 
    str1 = ", " 
    
    # return string   
    return (str1.join(s))

def kirim(request,*args,**kwargs):	
	if request.method =='POST':
		fruits = request.POST.getlist('cek')
		mode=""
		user=User.objects.all()
		ala = "C:/pln/Program Aktual/media_cdn/"
		if 'kirimMutasi' in request.POST:
			model = mutasi
			template='mutasi/pdf_mutasi.html'
			filename="mutasi.pdf"
			mode="kirim"
			tipe="email"
			redirek = 'mutasi:index'
			judul="SK Mutasi"	
			alamat=ala+'back up mutasi/'	

		elif 'kirimPLT' in request.POST:
			model = plt
			template='mutasi/pdf_plt.html'
			filename="plt.pdf"
			mode = "kirim"
			tipe="email"
			redirek = 'mutasi:plt'
			judul="Surat Penugasan PLT"
			alamat=ala+'back up PLT/'

		elif 'kirimAPS' in request.POST:
			model = aps
			template='mutasi/pdf_aps.html'
			filename="aps.pdf"
			mode = "kirim"
			tipe="email"
			redirek = 'mutasi:aps'
			judul="Surat Keputusan APS"
			alamat=ala+'back up APS/'

		elif 'kirimTalenta' in request.POST:
			model = talenta
			template='talenta/pdf_talenta.html'
			filename="talenta.pdf"
			mode = "kirim"
			tipe="email"
			redirek = 'talenta:index'
			judul="SK Kenaikan Grade/Level"
			alamat=ala+'back up talenta/'

		elif 'kirimKriteriaTalenta' in request.POST:
			model = kriteriaTalenta
			template='talenta/pdf_kriteriaTalenta.html'
			filename="kriteriaTalenta.pdf"
			mode = "kirim"
			tipe="email"
			redirek = 'talenta:kriteria'
			judul="Kriteria Talenta"
			alamat=ala+'back up kriteria talenta/'

		elif 'kirimPhDP' in request.POST:
			model = PhDP
			template='talenta/pdf_PhDP.html'
			filename="PhDP.pdf"
			mode = "kirim"
			redirek = 'talenta:PhDP'
			judul="PhDP"
			tipe="email"
			alamat=ala+'back up PhDP/'
			
		elif 'kirimMutasiWa' in request.POST:
			model = mutasi
			template='mutasi/pdf_mutasi.html'
			filename="mutasi.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'mutasi:index'
			judul="SK Mutasi"
			alamat=ala+'back up mutasi/'


		elif 'kirimPLTWa' in request.POST:
			model = plt
			template='mutasi/pdf_plt.html'
			filename="plt.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'mutasi:plt'
			judul="Surat Penugasan PLT"
			alamat=ala+'back up PLT/'

		elif 'kirimAPSWa' in request.POST:
			model = aps
			template='mutasi/pdf_aps.html'
			filename="aps.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'mutasi:aps'
			judul="Surat Keputusan APS"
			alamat=ala+'back up APS/'

		elif 'kirimTalentaWa' in request.POST:
			model = talenta
			template='talenta/pdf_talenta.html'
			filename="talenta.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'talenta:index'
			judul="SK Kenaikan Grade/Level"
			alamat=ala+'back up talenta/'

		elif 'kirimphdpTalentaWa' in request.POST:
			model = PhDP
			template='talenta/pdf_PhDP.html'
			filename="PhDP.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'talenta:PhDP'
			judul="PhDP"
			alamat=ala+'back up PhDP/'

		elif 'kirimKriteriaTalentaWa' in request.POST:
			model = kriteriaTalenta
			template='talenta/pdf_kriteriaTalenta.html'
			filename="kriteriaTalenta.pdf"
			mode = "kirim"
			tipe="wa"
			redirek = 'talenta:kriteria'
			judul="Kriteria Talenta"
			alamat=ala+'back up kriteria talenta/'

		elif 'hapusMutasi' in request.POST:
			model = mutasi			
			mode="hapus"
			redirek = 'mutasi:index'

		elif 'hapusPLT' in request.POST:
			model = plt
			mode = "hapus"
			redirek = 'mutasi:plt'

		elif 'hapusTalenta' in request.POST:
			model = talenta
			mode = "hapus"
			redirek = 'talenta:index'

		elif 'hapusPensiun' in request.POST:
			model = pensiun
			mode = "hapus"
			redirek = 'pensiun:index'
	

		if mode=="kirim":
			connection = mail.get_connection()
			connection.open()

			if tipe =="wa":
				whatsapp_login()
			pesanE = 0 
			pesanW = 0 
			emailGagal=0
			waGagal=0
			nipegEmailGagal=[]
			nipegWaGagal=[]
			for mu in fruits:
				try:
					mutate = model.objects.get(nipeg=mu)								
					if mutate.peg:											
						context={
							'sesuatu':mutate,
						}
						if judul=="SK Mutasi" or judul=="Surat Penugasan PLT" or judul=="Surat Keputusan APS":
							imail=mutate.email
							hp=mutate.noHp		
							nip=mutate.nipeg
							nam=mutate.nama
						elif judul =="Kriteria Talenta":
							imail=mutate.peg.email
							hp=mutate.peg.noHp
							nip=mutate.peg.nipeg
							nam=mutate.peg.nama
							context={
							'sesuatu':mutate,
							'tglAwal':tglKriteria.objects.get(posisi="awal"),
							'tglAkhir':tglKriteria.objects.get(posisi="akhir"),
							}
						else:
							imail=mutate.peg.email
							hp=mutate.peg.noHp
							nip=mutate.peg.nipeg
							nam=mutate.peg.nama
						print("Mengirim Email ke "+str(imail)+"...")						
						response=PDFTemplateResponse(request=request,
												 template=template,
												 filename =filename,
												 context=context,
												 show_content_in_browser=True,
												 cmd_options={'margin-top': 0,}
												 )
						
						with open(filename, 'wb') as f:
							f.write(response.rendered_content)

						date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
						date = date.strftime("D:%Y%m%d%H%M%S+00'00'")
						dct = {
							"aligned": 0,
							"sigflags": 3,
							"sigflagsft": 132,
							"sigpage": 0,
							"sigbutton": True,
							"sigfield": "Signature1",
							"sigandcertify": True,
							"signaturebox": (370, -100, 570, 640),
							"signature": "",
							"signature_img": "c:/pln3/aktual/static/image/ttd.jpg",
							"contact": "nyoman.astawa@pln.co.id",
							"location": "UID JATIM",
							"signingdate": date,
							"reason": judul,
							"password": "kambing212",
						}
						with open("selfsigned.pfx", "rb") as fp:
							p12 = pkcs12.load_key_and_certificates(
								fp.read(), b"kambing212", backends.default_backend()
							)				   
						datau = open(filename, "rb").read()
						datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha512")						
						with open(filename, "wb") as fp:
							fp.write(datau)
							fp.write(datas)
						attachment = open(filename, 'rb')									
						if (tipe == "email" and mail) or mutate.terkirim == False :	
							try:
								if (judul =="Kriteria Talenta"):												
									message=EmailMessage(judul+" "+nip,
										"Yth. Bapak/Ibu "+nam+" NIP "+nip+" \nPegawai PT PLN (Persero) Unit Induk Distribusi Jawa Timur \n\nDalam rangka mendukung proses efisiensi, efektifitas dan ketepatan dalam penyampaian Surat Keputusan (SK) \nmaka mulai tahun 2020 SK disampaikan melalui soft file kepada pegawai melalui email masing-masing \npegawai. \n\nTerlampir disampaikan Surat Keputusan tentang "+judul+" "+mutate.tglPeriode+" atas nama bapak/ibu "+nam+".\n Bilamana terdapat hal yang perlu dikonfirmasi dapat menghubungi pengelola SDM Unit Pelaksana setempat.\n\nEmail ini dikirim melalui sistem e-statement otomatis, mohon untuk tidak membalas. \n\nDemikian dan atas perhatian Bapak/Ibu diucapkan terima kasih. \n\n\n\nSalam, \n\nSub Bidang Administrasi SDM \nBidang SDM \nPT PLN (Persero) UID Jawa Timur \n",
										"SDM",[imail],connection=connection)
									
								else:
									message=EmailMessage(judul+" "+nip,
										"Yth. Bapak/Ibu "+nam+" NIP "+nip+" \nPegawai PT PLN (Persero) Unit Induk Distribusi Jawa Timur \n\nDalam rangka mendukung proses efisiensi, efektifitas dan ketepatan dalam penyampaian Surat Keputusan (SK) \nmaka mulai tahun 2020 SK disampaikan melalui soft file kepada pegawai melalui email masing-masing \npegawai. \n\nTerlampir disampaikan Surat Keputusan tentang "+judul+" atas nama bapak/ibu "+nam+".\n Bilamana terdapat hal yang perlu dikonfirmasi dapat menghubungi pengelola SDM Unit Pelaksana setempat.\n\nEmail ini dikirim melalui sistem e-statement otomatis, mohon untuk tidak membalas. \n\nDemikian dan atas perhatian Bapak/Ibu diucapkan terima kasih. \n\n\n\nSalam, \n\nSub Bidang Administrasi SDM \nBidang SDM \nPT PLN (Persero) UID Jawa Timur \n",
										"SDM",[imail],connection=connection)
									
								message.attach(filename,attachment.read(),'application/pdf')
								message.send()
								mutate.terkirim = True
								mutate.save()
								print("berhasil mengirim Email ke : "+str(imail))
								pesanE+=1
								shutil.copy(filename, alamat+mutate.peg.nipeg+".pdf")
							except:
								print("Pengiriman Email gagal")
								emailGagal+=1
								nipegEmailGagal.append(nip)

						if tipe =="wa" and hp:
							print("Mengirim wa nipeg : "+str(nip)+" dengan nomor HP : "+str(hp)+"...")
							try:							
								if (judul =="Kriteria Talenta"):
									send_message_to_unsavaed_contact(hp,"Yth Bapak/Ibu,\n\nSurat Keputusan tentang "+judul+" "+mutate.tglPeriode+" dengan NIP : "+nip+" telah dikirim melalui Email : " + imail+".\nDemikian sebagai informasi.\nTerima kasih.\n\nSalam,\nSub Bidang Administrasi SDM\nBidang SDM\nPT PLN (Persero) UID Jawa Timur",1)
								else:
									send_message_to_unsavaed_contact(hp,"Yth Bapak/Ibu,\n\nSurat Keputusan tentang "+judul+" dengan NIP : "+nip+" telah dikirim melalui Email : " + imail+".\nDemikian sebagai informasi.\nTerima kasih.\n\nSalam,\nSub Bidang Administrasi SDM\nBidang SDM\nPT PLN (Persero) UID Jawa Timur",1)
								pesanW+=1
								print("berhasil mengirim wa nipeg : "+str(nip)+" dengan nomor HP : "+str(hp))
							except:
								print("Pengiriman WA gagal")
								waGagal+=1	
								nipegWaGagal.append(nip)					
					else:
						messages.error(request, 'pegawai dengan nipeg '+ mutate.nipeg+' tidak memiliki email, pengiriman gagal')
						connection.close()	
				except:
					print("Pengiriman Gagal")	
					return redirect(redirek)
			
			if pesanE>0:
				print("telah mengirim email ke "+str(pesanE)+" pegawai")
				messages.success(request, 'Pesan Email telah terkirim ke '+ str(pesanE)+' pegawai')
				
			if pesanW>0:
				print("telah mengirim pesan WA ke "+str(pesanW)+" pegawai")
				messages.success(request, 'Pesan WA telah terkirim ke '+ str(pesanW)+' pegawai')
				
			if emailGagal>0:
				messages.error(request,"Pengiriman Email gagal ke pegawai dengan nipeg : "+listToString(nipegEmailGagal))
			if waGagal>0:
				messages.error(request,"Pengiriman WA gagal ke pegawai dengan nipeg : "+listToString(nipegWaGagal))

			connection.close()	
			if tipe =="wa":
				tutup()

		elif mode == "hapus" :			
			pesanH=0
			for mu in fruits:
				mutate = model.objects.get(nipeg=mu)
				mutate.delete()		
				pesanH+=1
			if pesanH>0:
				messages.success(request, 'Sebanyak '+ str(pesanH)+' SK telah dihapus')


	return redirect(redirek)

def relod(request,template):
	if template=='mutasi':
		mutas 	=mutasi.objects.all()
		judul	=mutasi
		redirek = 'mutasi:index'
	elif template=='plt':
		mutas 	=plt.objects.all()
		judul 	=plt
		redirek = "mutasi:plt"
	elif template =='PhDP':
		mutas =PhDP.objects.all()
		judul =PhDP
		redirek = "talenta:PhDP"
	elif template=='aps':
		mutas 	=aps.objects.all()
		judul 	=aps
		redirek = "mutasi:aps"
	elif template == "talenta":
		mutas 	=talenta.objects.all()
		judul 	=talenta
		redirek = "talenta:index"
	elif template == "pensiun":
		mutas 	=pensiun.objects.all()
		judul 	=pensiun
		redirek = "pensiun:index"
	elif template == "kriteriaTalenta":
		mutas 	=kriteriaTalenta.objects.all()
		judul 	=kriteriaTalenta
		redirek = "talenta:kriteria"

	pegg = pegawai.objects.all()
	pesanR=0
	pesanN=0
	pesanNipeg=[]
	#Menghapus data yang sama
	sis=mutas.values_list("nipeg", flat=True).distinct()
	for nipeg in sis:
		bab=judul.objects.filter(nipeg=nipeg).values_list('id',flat=True)[1:]
		mutas.filter(pk__in=list(bab)).delete()
	
	for a in mutas:
		
		try:
			b=pegg.get(nipeg=a.nipeg)
			a.peg = b
			a.save()
			pesanR+=1			
		except:
			a.peg = None
			a.save()
			pesanNipeg.append(a.nipeg)
			pesanN+=1
		
	if pesanR>0:
			messages.success(request, 'Berhasil me-reload '+ str(pesanR)+' pegawai')
	if pesanN>0:
			messages.success(request, 'Nipeg '+ str(pesanNipeg)+' tidak ada dalam Master Data Pegawai')
	return redirect(redirek)

	