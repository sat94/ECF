from django import forms
from .models import MyUser

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=10)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    nom = forms.CharField(max_length=10)
    prenom = forms.CharField(max_length=10)
    age = forms.IntegerField(max_value=99)
    email = forms.EmailField()
    adresse = forms.CharField(max_length=200)
    photo = forms.ImageField()
    cgu_accept = forms.BooleanField(initial=False)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$@#&" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de lettres spécial.")
        return pseudo

    def clean_nom(self):
        nom = self.cleaned_data.get("nom")
        if "$@#&" in nom:
            raise forms.ValidationError("Le nom ne peut pas contenir de lettres spécial.")
        return nom
    
    def clean_prenom(self):
        prenom = self.cleaned_data.get("prenom")
        if "$@#&" in prenom:
            raise forms.ValidationError("Le prénom ne peut pas contenir de lettres spécial.")            
        return prenom

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("Vous devez être majeur pour souscrire.")
        elif age > 80:
            raise forms.ValidationError("Vous avez pas taper l'age que vous avez.")
        return age

class inscription(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["pseudo", "password", "nom", "prenom", "age", "email", "adresse", "photo"]
        


