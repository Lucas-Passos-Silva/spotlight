# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Adicione o campo booleano 'validado'
    validado = models.BooleanField(default=False)
