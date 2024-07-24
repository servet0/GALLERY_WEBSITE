from django.shortcuts import render, redirect
from .models import firstRow

def home(request):
    firstrows = firstRow.objects.all().order_by("-date")

    context = {
        'firstrows': firstrows,
    }
    
    return render(request, 'base/home.html', context)

# Create your views here.
