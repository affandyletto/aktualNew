from django.db import models
from pegawai.models import pegawai
from django.contrib.auth import get_user_model

# Create your models here.

def upload_location(instance,filename):
	filename=instance.file.name
	return "%s/%s" %("pensiun", filename)

class pensiun(models.Model):
	nipeg		= models.CharField(max_length=20,default='')
	file 		= models.FileField(upload_to=upload_location,blank=True)
	terkirim	= models.BooleanField(default=False)
	peg 		= models.ForeignKey(pegawai,on_delete=models.SET_NULL, default="",blank=True,null = True)
	def __str__(self):
		return "{}".format(self.nipeg)