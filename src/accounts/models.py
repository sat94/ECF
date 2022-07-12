from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    pseudo = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    adresse = models.CharField(max_length=200)
    photo = models.ImageField()
    partenaire = models.BooleanField(default=False)

