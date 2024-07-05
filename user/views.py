from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.messages import constants as messages
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_django(request, user)
                return redirect('profile')
            else:
                msg= "Usuário ou senha inválidos"
        else:
            msg = "Formulário invalido"   
    return render(request, 'home.html', {'form':form, 'msg':msg})
