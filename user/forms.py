from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    username = forms.CharField(
        label='Usuário',  # Ajustando o label para 'Usuário'
        label_suffix='', 
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.EmailField(
        label='Email',  # Ajustando o label para 'Usuário'
        label_suffix='', 
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        label='Senha',  # Ajustando o label para 'Usuário'
        label_suffix='', 
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar senha',  # Ajustando o label para 'Usuário'
        label_suffix='', 
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',  # Ajustando o label para 'Usuário'
        label_suffix='',  # Removendo o sufixo padrão ':'
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        label='Senha',  # Ajustando o label para 'Senha'
        label_suffix='',  # Removendo o sufixo padrão ':'
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['avatar']