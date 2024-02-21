from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

def landing_page(request):
    context = {'user_logged_in': request.user.is_authenticated}
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'landing_page/index.html', context)

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'landing_page/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'landing_page/login.html', {'form': form})
