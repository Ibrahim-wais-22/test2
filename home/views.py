from typing import Reversible
from home.models import Blog
from django.shortcuts import render , redirect
from .models import Blog
from .forms import LoginForm,BlogForm
# Create your views here.

# def home(request):
#     query = Blog.objects.values("title")

#     # context = {}
#     return render(request , 'Templates/index.html' , {'titlee':query})

def home(request):
    blog_list = Blog.objects.all()
    context = {'blogs':blog_list}
    return render(request,'home/templates/home/index.html',context)

def blog(request,slug):
    article = Blog.objects.get(slug =slug)
    context = {'article':article}
    return render(request,'home/templates/home/blog.html',context)

def addblog(request):
    if request.method == 'POST':  ## save
        formadd = BlogForm(request.POST , request.FILES)
        if formadd.is_valid():
            myform = formadd.save(commit=False)
            myform.owner = request.user
            myform.save()
        return redirect('/home')
    else:
        formadd = BlogForm() 
    return render(request,'home/templates/home/addblog.html',{'formadd':formadd })
                        #   'home/templates/home/addblog.html' 
def login(request):
    if request.method == 'POST':  ## save
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(Reversible('home:addblog'))
    else:
        form = LoginForm() 
    return render(request,'home/templates/home/login.html',{'form':form})
