from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from user.models.user import Usuario
from .forms import TweetForm
from tweet.models import Tweet

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

@login_required 
def delete_tweet(request, pk):
    usuario = request.user
    tweet = get_object_or_404(Tweet, pk=pk, author=usuario)

    if request.method == 'POST':
        tweet.delete()
        return redirect('detail')
    

@login_required
def tweet_update(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk, author=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('detail')
    else:
        form = TweetForm(instance=tweet)

    context = {
        'form': form,
        'tweet': tweet
    }
    return render(request, 'tweet_update.html', context)
