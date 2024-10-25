from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import profile


#in froma class hast bara hamin bayad to view ke mikhay estfde konim instance besazim


#ba in kar ye field email ezafe kardim be defualt form ke dashtim
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #migim ba in meta taqirat to model user etefaq biofte
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email"]



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ["image"]