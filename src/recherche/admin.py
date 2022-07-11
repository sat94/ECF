from django.contrib import admin
from .models import Entreprise, UserProfile

admin.site.register(UserProfile)

admin.site.register(Entreprise)

