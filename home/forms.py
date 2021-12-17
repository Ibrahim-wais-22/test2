from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Blog ,The_user

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ['title','contant','image']
        fields = ['title','contant','image']
        # execlude = ('slug','owner',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = The_user
        fields = ['name','email','password']
        
    