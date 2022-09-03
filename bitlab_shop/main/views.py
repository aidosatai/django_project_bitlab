from django.shortcuts import render
# from django.http import
from .models import Category


def home(request):
    category=Category.objects.all()
    return render(request, 'index.html', context={'category':category})





