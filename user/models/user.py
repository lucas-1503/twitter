from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following'
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.first_name

    def follow(self, user):
        """Seguir um usuário"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Deixar de seguir um usuário"""
        if user != self:
            self.following.remove(user)