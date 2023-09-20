from django.shortcuts import render

# Create your views here.

def index_view(response):
    
    return render(response, "core/index.html") 

def signup_view(response): 
    return render(response, 'core/signup.html')

def signin_view(response): 
    return render(response, 'core/signin.html')
