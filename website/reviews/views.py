from django.shortcuts import render
from .models import Company


def home(request):
    return render(request, 'reviews/home.html')

def info(request):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'reviews/info.html', context)

def ranking(request):
    return render(request, 'reviews/ranking.html')

def about(request):
    return render(request, 'reviews/about.html')
