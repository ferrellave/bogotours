from django import forms
from web.models import Item

class FormularioContacto(forms.Form):

    correo = forms.EmailField(
        label='Correo', 
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    mensaje = forms.CharField(
        label='Mensaje', 
        widget=forms.Textarea(attrs={'class':'form-control'})
        )

class Bookingform(forms.Form):

	item = forms.ModelChoiceField(queryset=Item.objects.all(),label="Select a Tour",required=True)
	date = forms.DateField(
        label='¿Qué dia prefiere agendar?', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	tickets = forms.CharField(
        label='¿Cuantas personas vienen con usted?', 
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
	first = forms.CharField(
        label='¿Cual es su nombre?', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	last = forms.CharField(
        label='Cual es su Apellido?', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	phone = forms.CharField(
        label='Indiquenos un numero de contacto', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	email = forms.EmailField(
        label='Indiquenos un Email', 
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
	message = forms.CharField(
        label='Por favor escriba un mensaje adicional', 
        widget=forms.Textarea(attrs={'class':'form-control'})
        )