from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Category, Task
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    
    return render(request, "core/index.html") 

def signup_view(request):  
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        
        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('home')
            
    return render(request, 'core/signup.html')
    



def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'core/signin.html') 

@login_required 
def home_view(request):
    return render(request, 'core/home.html')

@login_required
def profile_view(request):
    return render(request, 'core/profile.html')

@login_required 
def create_task_view(request):
    return render(request, 'core/task.html') 


# @login_required
def signout_view(request):
    logout(request)
    return render(request, 'core/signout.html')

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)