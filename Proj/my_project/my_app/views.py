from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправте користувача на головну сторінку
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Повертаємо користувача на головну сторінку після створення допису
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
