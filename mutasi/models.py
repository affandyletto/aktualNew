from django.db import models
from pegawai.models import pegawai

class mutasi(models.Model):
	no 				=models.IntegerField(default=1,blank=True,null=True)
	nipeg			=models.CharField(max_length=100,default='')
	nama			=models.CharField(max_length=255,default="")
	jabatanSekarang	=models.CharField(max_length=255,default='')
	grade			=models.CharField(max_length=255,default='')
	tglJabTer		=models.CharField(max_length=255,default='')
	PendidikanTer	=models.CharField(max_length=255,default='',blank=True,null=True)
	jabatanBaru		=models.CharField(max_length=255,default='')
	keterangan		=models.CharField(max_length=255,default='')
	noSk			=models.CharField(max_length=255,default='')
	tglSk			=models.CharField(max_length=255,default='')
	tglBerlaku		=models.CharField(max_length=255,default='')
	unit			=models.CharField(max_length=255,default='')
	jenjang			=models.CharField(max_length=255,default='')
	terkirim		=models.BooleanField(default=False)
	email			=models.CharField(max_length=255,default='')
	noHp			=models.CharField(max_length=255,default='')
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)

class aps(models.Model):
	no 				=models.IntegerField(default=1,blank=True,null=True)
	nipeg			=models.CharField(max_length=100,default='')
	nama			=models.CharField(max_length=255,default="")
	jabatanSekarang	=models.CharField(max_length=255,default='')
	grade			=models.CharField(max_length=255,default='')
	tglJabTer		=models.CharField(max_length=255,default='')
	PendidikanTer	=models.CharField(max_length=255,default='',blank=True,null=True)
	jabatanBaru		=models.CharField(max_length=255,default='')
	keterangan		=models.CharField(max_length=255,default='')
	noSk			=models.CharField(max_length=255,default='')
	tglSk			=models.CharField(max_length=255,default='')
	tglBerlaku		=models.CharField(max_length=255,default='')
	unitLama		=models.CharField(max_length=255,default='')	
	unitPengirim	=models.CharField(max_length=255,default='')
	noPengirim		=models.CharField(max_length=255,default='')
	unitPenerima	=models.CharField(max_length=255,default='')
	noPenerima		=models.CharField(max_length=255,default='')
	terkirim		=models.BooleanField(default=False)
	email			=models.CharField(max_length=255,default='')
	noHp			=models.CharField(max_length=255,default='')
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)


class plt(models.Model):
	no 				=models.IntegerField(default=1,blank=True,null=True)
	nipeg 			=models.CharField(max_length=100,default='')
	nama			=models.CharField(max_length=255,default="")
	nomorPLT		=models.CharField(max_length=100,default='')
	tglPLT			=models.CharField(max_length=255,default='')
	jabatanTanpaPLT	=models.CharField(max_length=255,default='')
	jabatanPLT 		=models.CharField(max_length=255,default='')
	terkirim		= models.BooleanField(default=False)
	email			=models.CharField(max_length=255,default='')
	noHp			=models.CharField(max_length=255,default='')
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)
