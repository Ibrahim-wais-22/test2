from django.shortcuts import render
from home.models import Blog


def articals(request):
    artical_list = Blog.objects.all()
    context = {'articals':artical_list}
    # return render(request,'artical/templates/index.html',context)
    return render(request,'home/templates/index.html',context)
