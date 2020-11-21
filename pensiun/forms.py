from django import forms
from .models import pensiun

class pensiunForm(forms.ModelForm): 
    file=forms.FileField(widget=forms.FileInput(
        attrs={
            'multiple':True,            
        }
        ))
    nipeg=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 form-control'
        }

        ))
    class Meta:
    	model=pensiun
    	fields = [
            "file",
            "nipeg",
        ]