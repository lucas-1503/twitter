from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from user.models.user import Usuario
from .forms import TweetForm
from tweet.models import Tweet

@login_required
def profile_view(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    seguidores = user.followers.all()
    seguindo = request.user.following.all()
    usuarios = Usuario.objects.exclude(pk=request.user.pk).exclude(pk__in=seguindo)
    tweets = Tweet.objects.filter(author__in=seguindo).exclude(author = request.user).order_by('-created_at')
    
    context = {
        'user': user,
        'seguidores': seguidores,
        'usuarios': usuarios,
        'seguindo':seguindo,
        'tweets':tweets,
    }
    return render(request, 'profile.html', context)

@login_required
def send_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            return redirect('profile', pk=request.user.pk)  # Redireciona para o perfil do usuário
    else:
        form = TweetForm()
    
    return render(request, 'create_tweet.html', {'form': form})

def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)

    if request.method == 'POST':
        tweet.delete()
        # Redireciona para a página detalhada do usuário após a exclusão
        return redirect('detail')

@login_required    
def feed_view(request, pk ):
    user = get_object_or_404(Usuario, pk=pk)
    seguindo = request.user.following.all()
    tweets = Tweet.objects.filter(author__in=seguindo).exclude(author = request.user).order_by('-created_at')

    context = {
        'user': user,
        'seguindo':seguindo,
        'tweets':tweets,
    }
    return render(request, 'feed.html', context)