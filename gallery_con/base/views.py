from django.shortcuts import render, redirect

def home(request):
    
    return render(request, 'base/home.html')

# Create your views here.
