from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom','prenom','age','email','option']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'from-control'}),
            'prenom': forms.TextInput(attrs={'class':'from-control'}),
            'age': forms.TextInput(attrs={'class':'from-control'}),
            'email': forms.EmailInput(attrs={'class':'from-control'}),
            'option': forms.TextInput(attrs={'class':'from-control'}),
            
        }