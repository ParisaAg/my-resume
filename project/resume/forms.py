from django import forms
from resume.models import *


class NameForm(forms.Form):
    name = forms.CharField(label='name:',max_length=255)
    email= forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.TextInput()
    



class ContactForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model=contact
        fields="__all__"