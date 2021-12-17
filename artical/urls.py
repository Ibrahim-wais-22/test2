from django.urls import path 
from . import views
app_name = 'artical'
urlpatterns = [
    path('',views.articals ),
    # path('<str:slug>',views.blog ,name='blog' ),
]
