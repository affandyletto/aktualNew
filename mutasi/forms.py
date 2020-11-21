from django.forms import ModelForm
from django import forms
from .models import mutasi,plt,aps

class mutasiForm(ModelForm):
	nipeg=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	nama=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	jabatanSekarang=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'

		}
		))

	grade=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	tglJabTer=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))


	jabatanBaru=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'
		}
		))
	keterangan=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	noSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))	
	tglSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglBerlaku=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))

	unit=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))		
	
	jenjang=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',			
		}
		))
	email=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',			
		}
		))
	noHp=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',			
		}
		))
	class Meta:
		model = mutasi
		fields = [
			'nipeg',
			'nama',
			'jabatanSekarang',
			'grade',
			'tglJabTer',
			'PendidikanTer',
			'jabatanBaru',
			'keterangan',
			'noSk',
			'tglSk',
			'tglBerlaku',
			'unit',
			'jenjang',
			'email',
			'noHp'
		]

class apsForm(ModelForm):
	nipeg=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	nama=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	jabatanSekarang=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'

		}
		))

	grade=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	tglJabTer=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))


	jabatanBaru=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'
		}
		))
	keterangan=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	noSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))	
	tglSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglBerlaku=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))

	unitLama=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))		
	unitPengirim=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))	
	noPengirim=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))	
	unitPenerima=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))	
	noPenerima=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))

	email=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',			
		}
		))
	noHp=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',			
		}
		))
	class Meta:
		model = aps
		fields = [
			'nipeg',
			'nama',
			'jabatanSekarang',
			'grade',
			'tglJabTer',
			'PendidikanTer',
			'jabatanBaru',
			'keterangan',
			'noSk',
			'tglSk',
			'tglBerlaku',
			'unitLama',
			'unitPengirim',
			'noPengirim',
			'unitPenerima',
			'noPenerima',
			'email',
			'noHp'
		]
	

class pltForm(ModelForm):
	nipeg=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	nama=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	nomorPLT=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	tglPLT=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	jabatanTanpaPLT=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'

		}
		))
	jabatanPLT=forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'mb-2 form-control ',
			'cols':"30",
			'rows' :'5'

		}
		))
	email=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	noHp=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	
	class Meta:
		model = plt
		fields = [
			'nipeg',
			'nama',
			'nomorPLT',
			'tglPLT',
			'jabatanTanpaPLT',
			'jabatanPLT',
			'email',
			'noHp'
		]