from .models import Admin
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect



def admins_list(request):
    return render(request, 'accounts/admins_list.html')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # أو الصفحة اللي عايز تروح لها بعد التسجيل
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Sign Up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # بعد ما يسجل يروح صفحة اللوجين
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

