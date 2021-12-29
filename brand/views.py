from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def brand(request):
    return render(request, 'brand.html')

def brand_users(request):
    
    if request.method == 'POST':
        brand = UserCreationForm(request.POST)
        if brand.is_valid():
            username = brand.cleaned_data.get('username')
            messages.success(request, f'user is successuly registered as { username }')

    else:
        brand =UserCreationForm()
        return render(request, 'brand_users.html',{'userbrand':brand})

    
