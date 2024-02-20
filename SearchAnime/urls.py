from django.urls import path
from . import views

app_name = "SearchAnime"
urlpatterns = [
    path('',views.search,name='search'),
    path('detail/<str:pk>',views.detail,name="detail"),
]
