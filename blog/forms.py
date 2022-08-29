from dataclasses import field
from pyexpat import model
from turtle import hideturtle
from django import forms
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.models import User

from .models import Avatar, Reparacion

class clienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    vehiculo = forms.CharField()
    desperfecto = forms.CharField()

class MecanicoFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField() 



class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget =forms.HiddenInput(), required= False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if (password2 != self.cleaned_data["password1"]):
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return password2



class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)


class ReparacionFormulario(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields= ('imagen',)

    