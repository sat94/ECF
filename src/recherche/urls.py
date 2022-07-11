from django.urls import path
from .views import recherche


urlpatterns = [
   path('', recherche, name="recherche"),   
]
