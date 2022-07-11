
from django.contrib import admin
from .views import index
from accounts.views import signup
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('sport-admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('partenaire/', include("recherche.urls"),name="partenaire"),   
]
