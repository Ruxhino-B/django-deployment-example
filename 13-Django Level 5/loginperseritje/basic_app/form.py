from django import forms
from django.contrib.auth.models import User
from basic_app.models import ProfilUseriInfo

class FormUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class FormProfilUserInfo(forms.ModelForm):
    class Meta():
        model = ProfilUseriInfo
        fields= ('adrese_webi','Foto')
