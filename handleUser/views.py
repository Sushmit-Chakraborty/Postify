from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',{'form':form})

def user_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('displayPosts')
    except:
        print("Error")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request,user)
                    return redirect('displayPosts')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login/')
def restrictedView(request):
    return HttpResponse("Secret Found")