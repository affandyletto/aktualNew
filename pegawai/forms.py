from django import forms
from .models import pegawai

class pegawaiForm(forms.ModelForm): 
    no=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    nipeg=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    nama=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    unit=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    email=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    noHp=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    class Meta:
    	model=pegawai
    	fields = [
            "no",
            "nipeg",
            "nama",
            "unit",
            "email",
            "noHp",
        ]