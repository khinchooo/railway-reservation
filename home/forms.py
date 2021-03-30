from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())

class UserRegister(forms.ModelForm):
    number=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','password','email','number']

    def LoginButton(self, commit=True):
        user = super(UserRegister, self).save(commit=False)
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user