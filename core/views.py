from django.shortcuts import render

# Create your views here.

def index_view(response):
    
    return render(response, "core/index.html")