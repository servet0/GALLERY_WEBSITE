from django.shortcuts import render, redirect
from .models import firstRow, secondRow

def home(request):
    firstrows = firstRow.objects.all().order_by("-date")
    secondrows = secondRow.objects.all().order_by("-date")

    context = {
        'firstrows': firstrows,
        'secondrows': secondrows,
    }
    
    return render(request, 'base/home.html', context)

# Create your views here.
