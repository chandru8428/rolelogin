from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_home')
            else:
                return redirect('user_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_home')
            else:
                return redirect('user_home')
    return render(request, 'login.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def user_home(request):
    return render(request, 'user_home.html')

from django.shortcuts import redirect

def home(request):
    return redirect('login')  # or use 'register'
