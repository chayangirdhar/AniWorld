from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import User_login,Register_user
from .models import AnimeDatabase
# Create your views here.


def home(request):
    
    website_data = {}
    return render(request,'Core/index.html',website_data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password= password)
        if user is not None:
            login(request,user)
            return redirect('Core:home')
    else:
        form = User_login()
    
    website_data = {'form':form,
    'title':'Login'}
    return render(request,'Core/login.html',website_data)

def user_logout(request):
    logout(request)
    return redirect('Core:home')

def RegisterUser(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username,password = password)
            login(request,user)
            return redirect('core:index')
    else:
        form = Register_user()
    website_data = {
        'form': form,
        'title': "Register"
    }
    return render(request,'Core/register.html',website_data)

