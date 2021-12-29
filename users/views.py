from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def users(request):
    return render(request,'firstPage.html',{'name':'AlieSoft'})

def register(request):
    
    form = UserCreationForm()
    return render(request,'register.html',{'names':form})