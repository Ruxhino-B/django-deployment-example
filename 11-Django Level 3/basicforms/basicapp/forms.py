from django import forms
from django.core import validators

#Rasti kur ne duam qe te bejne shkrim vetem ata qe kan emrin me Z
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name need to start with Z')

class FormName(forms.Form):
    #Kjo funksionon vetem ne rastim me siper nqs ne duam emrat qe fillojne me Z
    # name = forms.CharField(validators= [check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required = False,widget=forms.HiddenInput,
    #                                 validators=[validators.MaxLengthValidator(0)])

#program i bere vete me kap rrobot
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('KAPEM NJE RROBOT')
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Sigurohu qe Emailet perputhen...")
