from itertools import count
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from tweet.models import Tweet
from django.db.models import Q



from user.models.user import Usuario
from .forms import LoginForm, UsuarioForm, AvatarForm

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
                return redirect('profile', pk=user.pk) 
            else:
                msg = "Usuário ou senha inválidos"
        else:
            msg = "Formulário inválido"   
    return render(request, 'home.html', {'form': form, 'msg': msg})

def register_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')  # Redirecione para a página inicial ou qualquer outra página após o login
    else:
        form = UsuarioForm()
    return render(request, 'register.html', {'form': form})

@login_required
def detail_view(request):
    # Recupere o usuário logado
    usuario = request.user

    # Recupere os tweets do usuário
    tweets = Tweet.objects.filter(author=usuario).order_by('-created_at')

    # Renderize o template com os detalhes do usuário e os tweets
    context = {
        'usuario': usuario,
        'tweets': tweets,
    }
    return render(request, 'detail.html', context)

@login_required
def alterar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('detail')  # Redireciona de volta para a página de detalhes do usuário
    else:
        form = AvatarForm(instance=request.user)
    
    return render(request, 'detail.html', {'form': form})

@login_required
def follow_user(request, pk):
    user_to_follow = get_object_or_404(Usuario, pk=pk)
    request.user.follow(user_to_follow)
    return redirect('user-list', pk=request.user.pk)

@login_required
def unfollow_user(request, pk):
    user_to_unfollow = get_object_or_404(Usuario, pk=pk)
    request.user.unfollow(user_to_unfollow)
    return redirect('user-list', pk=request.user.pk)

@login_required
def profile_view(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    seguidores = user.followers.all()
    seguindo = request.user.following.all()
    usuarios = Usuario.objects.exclude(pk=request.user.pk).exclude(pk__in=seguindo)
    tweets = Tweet.objects.filter(author__in=seguindo).exclude(author=request.user).order_by('-created_at')
    

    context = {
        'user': user,
        'seguidores': seguidores,
        'usuarios': usuarios,
        'seguindo': seguindo,
        'tweets': tweets,
    }
    return render(request, 'profile.html', context)

@login_required
def user_list(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    seguindo = request.user.following.all()
    query = request.GET.get('search', '')

    if query:
        usuarios = Usuario.objects.filter(
            Q(username__icontains=query) 
        ).exclude(pk=request.user.pk)
    else:
        usuarios = Usuario.objects.exclude(pk=request.user.pk)

    context = {
        'user': user,
        'usuarios': usuarios,
        'seguindo': seguindo,
    }
    return render(request, 'user_list.html', context)
