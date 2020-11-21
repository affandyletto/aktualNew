from django.db import models

# Create your models here.

class pegawai(models.Model):
	no 		=models.IntegerField(default=1,blank=True,null=True)
	nipeg	= models.CharField(max_length=100, default="")
	nama	= models.CharField(max_length=100, default="")
	unit	= models.CharField(max_length=100, default="")
	email	= models.CharField(max_length=100, default="")
	noHp	= models.CharField(max_length=255,default='')
	numUnit	= models.CharField(default="", max_length=50,blank=True)
	num 	= models.CharField(default="", max_length=50,blank=True)
	def __str__(self):
		return "{} . {} ".format(self.nipeg, self.nama)

