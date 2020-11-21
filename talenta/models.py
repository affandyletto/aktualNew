from django.db import models
from pegawai.models import pegawai
# Create your models here.
class talenta(models.Model):
	no 				=models.IntegerField(default=1)
	nipeg			=models.CharField(max_length=50,default='')
	nama			=models.CharField(max_length=100,default="")
	jenjangMayoritas=models.CharField(max_length=255,default='')
	jabatanSekarang	=models.CharField(max_length=255,default='')
	jenjangSebelum	=models.CharField(max_length=255,default='')
	gradeSebelum	=models.CharField(max_length=100,default='',blank=True,null=True)
	skalaGajiSebelum=models.CharField(max_length=100,default='')
	tglGrade		=models.CharField(max_length=100,default='')
	g1				=models.CharField(max_length=5,default='',blank=True,null=True)
	g2				=models.CharField(max_length=5,default='',blank=True,null=True)
	g3				=models.CharField(max_length=5,default='',blank=True,null=True)
	g4				=models.CharField(max_length=5,default='',blank=True,null=True)
	g5				=models.CharField(max_length=5,default='',blank=True,null=True)
	g6				=models.CharField(max_length=5,default='',blank=True,null=True)
	g7				=models.CharField(max_length=5,default='',blank=True,null=True)
	g8				=models.CharField(max_length=5,default='',blank=True,null=True)
	jenjangSesudah	=models.CharField(max_length=30,default='')
	gradeSesudah	=models.CharField(max_length=30,default='')
	skalaGajiSesudah=models.CharField(max_length=30,default='')
	tglNaik			=models.CharField(max_length=30,default='')
	naikPer			=models.CharField(max_length=30,default='')
	keterangan		=models.CharField(max_length=80,default='')
	noSk			=models.CharField(max_length=100,default='')
	tglSkKenaikan	=models.CharField(max_length=30,default='')
	noSkNaik		=models.CharField(max_length=30,default='')
	tglPeriode		=models.CharField(max_length=100,default='')
	tglBerlaku		=models.CharField(max_length=100,default='')
	terkirim		=models.BooleanField(default=False)
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)	
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)

class kriteriaTalenta(models.Model):
	no 				=models.IntegerField(default=1)
	nipeg			=models.CharField(max_length=50,default='')
	nama			=models.CharField(max_length=100,default="")
	grade 			=models.CharField(max_length=100,default='',blank=True,null=True)
	g1				=models.CharField(max_length=200,default='',blank=True,null=True)
	g2				=models.CharField(max_length=200,default='',blank=True,null=True)
	g3				=models.CharField(max_length=200,default='',blank=True,null=True)
	g4				=models.CharField(max_length=200,default='',blank=True,null=True)
	g5				=models.CharField(max_length=200,default='',blank=True,null=True)
	g6				=models.CharField(max_length=200,default='',blank=True,null=True)
	g7				=models.CharField(max_length=2005,default='',blank=True,null=True)
	g8				=models.CharField(max_length=200,default='',blank=True,null=True)
	noSk			=models.CharField(max_length=100,default='')
	tglSk			=models.CharField(max_length=100,default='')
	tglBerlaku		=models.CharField(max_length=100,default='')
	tglPeriode		=models.CharField(max_length=100,default='')
	terkirim		=models.BooleanField(default=False)
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)

class PhDP(models.Model):
	no 				=models.IntegerField(default=1)
	nipeg			=models.CharField(max_length=50,default='')
	periode 		=models.CharField(max_length=100,default='')
	nama			=models.CharField(max_length=100,default="")
	grade 			=models.CharField(max_length=100,default='',blank=True,null=True)
	skalaLama 		=models.CharField(max_length=100,default="")
	skalaBaru		=models.CharField(max_length=100,default="")
	noSk 			=models.CharField(max_length=100,default="")
	tglBerlaku 		=models.CharField(max_length=100,default="")
	tglSk  			=models.CharField(max_length=100,default="")
	terkirim		=models.BooleanField(default=False)
	peg 			=models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	def __str__(self):
		return "{} . {}".format(self.nipeg,self.nama)

class tglKriteria(models.Model):
	tgl1				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl2				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl3				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl4				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl5				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl6				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl7				=models.CharField(max_length=100,default='',blank=True,null=True)
	tgl8				=models.CharField(max_length=100,default='',blank=True,null=True)
	posisi				=models.CharField(max_length=100,default='',blank=True,null=True)
	def __str__(self):
		return "{}".format(self.tgl1)