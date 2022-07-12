from telnetlib import AUTHENTICATION
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render
from accounts.forms import SignupForm, inscription

def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'index.html')
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})

   
def inscrip(request):
    form = inscription()

    return render(request, "inscription.html",{"form" : form})

def logout_user(request):
    logout(request)
    return redirect('index')