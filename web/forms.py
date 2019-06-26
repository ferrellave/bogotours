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

	item = forms.ModelChoiceField(queryset=Item.objects.all(),label="Choose a Tour",required=True)
	date = forms.DateField(
        label='Date', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	tickets = forms.CharField(
        label='Tickets', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	first = forms.CharField(
        label='Firstname', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	last = forms.CharField(
        label='Lastame', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	phone = forms.CharField(
        label='Phone', 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
	email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
	message = forms.CharField(
        label='Message', 
        widget=forms.Textarea(attrs={'class':'form-control'})
        )