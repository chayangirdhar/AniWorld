from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class User_login(AuthenticationForm):
    username = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class' : 'form-control'}), label='')
    password = forms.CharField(required=True,widget=forms.widgets.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class' : 'form-control'}), label='')

    class Meta:
        model = User

class Register_user(UserCreationForm):
    first_name = forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control class-col'}), label='')
    last_name = forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control class-col'}), label='')
    email = forms.CharField(required=True, widget= forms.widgets.EmailInput(attrs={
        'placeholder': 'Email ID',
        'class': 'form-control class-col'}), label='')
    phone = forms.CharField(required=True, widget= forms.widgets.NumberInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'form-control class-col'}), label='')
    username = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={
        'placeholder':'Enter username',
        "class":"form-control"}), label="")
    password1 = forms.CharField(required=True , widget= forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
           "class":"form-control"}), label="",help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>')
    password2 = forms.CharField(required=True , widget= forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
           "class":"form-control"}), label="",help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone','password1','password2',)