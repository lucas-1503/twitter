from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following'
    )

    def __str__(self):
        return self.first_name