
from django.db import models

class UserProfile(models.Model):
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=30, primary_key=True)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Administrateur"

    def __str__(self):
        return self.user.username

class Entreprise(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='image_publie', blank=True, null=True)
    photo = models.ImageField(upload_to='image_publie', blank=True, null=True)
    description =  models.CharField(max_length=200)
    small_description =  models.CharField(max_length=90)
    dpo = models.CharField(max_length=50)
    technical_contact = models.CharField(max_length=50)
    commercial_contact = models.CharField(max_length=50)
    member = models.IntegerField(default=0)
    staff = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name