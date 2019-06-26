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
        label='Date of Tour', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	tickets = forms.CharField(
        label='Number of Persons', 
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
	first = forms.CharField(
        label='Your First Name', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	last = forms.CharField(
        label='Your Last Name', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	phone = forms.CharField(
        label='Your Phone Number', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	email = forms.EmailField(
        label='Your Email', 
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
	message = forms.CharField(
        label='Aditional Message', 
        widget=forms.Textarea(attrs={'class':'form-control'})
        )