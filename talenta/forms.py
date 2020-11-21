from django.forms import ModelForm
from django import forms
from .models import talenta,kriteriaTalenta

class talentaForm(ModelForm):
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

	jenjangMayoritas=forms.CharField(widget=forms.TextInput(
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

	gradeSebelum=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

	skalaGajiSebelum=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '
		}
		))

	tglGrade=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))


	g3=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g4=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g5=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g6=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g7=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g8=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	jenjangSesudah=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	gradeSesudah=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	skalaGajiSesudah=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglNaik=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	naikPer=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	keterangan=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	noSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	noSkNaik=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglPeriode=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglBerlaku=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	class Meta:
		model = talenta
		fields = [
			'nipeg',
			'nama',
			'jenjangMayoritas',
			'jabatanSekarang',
			'jenjangSebelum',
			'gradeSebelum',
			'skalaGajiSebelum',
			'tglGrade',
			'g3',
			'g4',
			'g5',
			'g6',
			'g7',
			'g8',
			'jenjangSesudah',
			'gradeSesudah',
			'skalaGajiSesudah',
			'tglNaik',
			'naikPer',
			'keterangan',
			'noSk',
			'tglSkKenaikan',
			'noSkNaik',
			'tglPeriode',
			'tglBerlaku'
		]
	
class kriteriaForm(ModelForm):
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

	grade=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))
	g1=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g2=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	g3=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g4=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g5=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g6=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g7=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	g8=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	noSk=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglPeriode=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglBerlaku=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	class Meta:
		model = kriteriaTalenta
		fields = [
			'nipeg',
			'nama',
			'grade',
			'g1',
			'g2',
			'g3',
			'g4',
			'g5',
			'g6',
			'g7',
			'g8',
			'noSk',
			'tglPeriode',
			'tglBerlaku'
		]



class PhDPForm(ModelForm):
	periode=forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control ',
		}
		))

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
	grade=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	skalaLama=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	skalaBaru=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	noSk=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglBerlaku=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	tglSk=forms.CharField(required=False,widget=forms.TextInput(
		attrs={
			'class':'mb-2 form-control '			
		}
		))
	
	
	class Meta:
		model = kriteriaTalenta
		fields = [
			'periode',
			'nipeg',
			'nama',
			'grade',
			'skalaLama',
			'skalaBaru',
			'noSk',
			'tglBerlaku',
			'tglSk'
		]