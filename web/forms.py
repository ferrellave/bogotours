# -*- encoding: utf-8 -*-
from django import forms
from web.models import Item, UserProfile
from django.contrib.auth.models import User

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

	item = forms.ModelChoiceField(queryset=Item.objects.all(),label="Seleccione el Tour de su preferencia",required=True)
	date = forms.DateField(
        label='¿Que dia prefiere agendar?', 
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

class signup_form(forms.Form):
    username = forms.EmailField(
        label='Email',
        min_length=1,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(
        label='Name',
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Repeat Password',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Email already exist')
        return username
    def clean_nickname(self):
        """Comprueba que no exista un email igual en la db"""
        nickname = self.cleaned_data['nickname']
        if UserProfile.objects.filter(nickname=nickname):
            raise forms.ValidationError('Nickname already exist')
        return nickname
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Make sure your password match')
        return password2