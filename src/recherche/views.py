from django.shortcuts import render

def recherche(request):
    return render(request, 'recherche.html')