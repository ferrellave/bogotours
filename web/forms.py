from django import forms

class FormularioContacto(forms.Form):

    correo = forms.EmailField(
        label='Correo', 
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    mensaje = forms.CharField(
        label='Mensaje', 
        widget=forms.Textarea(attrs={'class':'form-control'})
        )