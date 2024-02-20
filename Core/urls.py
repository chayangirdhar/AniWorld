from django.urls import path
from . import views

app_name = 'Core'

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('register',views.RegisterUser,name='register'),
    path('logout',views.user_logout,name='logout'),

]

