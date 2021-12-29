from django.shortcuts import render
from .models import News
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def public(request):
    
    context = {
       'news' : News.objects.all() 
    }
    return render(request,'home.html', context)

def about (request):
    return render(request, 'about.html')

def registration_form(request):
    
    forms= UserCreationForm()
    return render(request, 'registration_form.html',{'name':forms})
    
