from django import forms
from basicapp2.models import Users

class NewUsers(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
