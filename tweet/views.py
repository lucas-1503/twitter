from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from user.models.user import Usuario

@login_required
def profile_view(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    seguidores = user.followers.all()
    seguindo = request.user.following.all()
    usuarios = Usuario.objects.exclude(pk=request.user.pk).exclude(pk__in=seguindo)
    
    context = {
        'user': user,
        'seguidores': seguidores,
        'usuarios': usuarios,
        'seguindo':seguindo,
    }
    return render(request, 'profile.html', context)

def send_tweet(request):
    return render('profile')
