from django.urls import path 
from . import views
app_name = 'Home'

urlpatterns = [
    path('',views.home ),
    path('login',views.login ,name='login' ),
    path('addblog',views.addblog ,name='addblog' ),
    path('<str:slug>',views.blog ,name='blog' ),
]
