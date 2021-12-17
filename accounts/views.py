from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import SigunpForm
from django.contrib.auth import authenticate, login
# Create your views here.
def signup(request):
    if request.method=="post":
        form = SigunpForm(request.POST)
        if form.is_valid:
            print('done!!#################3')
            form.save()
            print('done!!!!!!!!!!!!!!!')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            # authenticate
            login(request,user)
            return redirect('/accounts/profile.html')

    else:
        form = SigunpForm()
    return render(request ,'registration/signup.html',{'form':form} )