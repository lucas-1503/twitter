from django.db import models
from user.models.user import Usuario
from django.utils import timezone

class Tweet(models.Model):
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='twits')
    content = models.TextField(max_length=280)  # Limite de 280 caracteres como o Twitter
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author.username}: {self.content[:50]}'
    
    class Meta:
        db_table = 'tweet'
    
    