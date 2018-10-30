from django import forms
from .models import Post
from django.contrib.auth.models import User

class Postform(forms.ModelForm):

    class Meta:
        model=Post
        fields=['text','title']

class Userform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']
