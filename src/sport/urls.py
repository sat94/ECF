
from django.contrib import admin
from .views import index
from accounts.views import signup, logout_user,login
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('sport/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout_user, name="logout"),
    path('partenaire/', include("recherche.urls"),name="partenaire"),   
]
