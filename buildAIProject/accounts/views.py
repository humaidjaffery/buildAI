from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup_view(request):
    user = request.user
    if user.is_authenticated:
        messages.warning(request, 'You are aleady logged in')
        return redirect('home') 
      
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username') 
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, type=type, password=raw_password)
            login(request, account)
            return redirect('home')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    user = request.user
    if user.is_authenticated:
        messages.warning(request, 'You are aleady logged in')
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account:
            login(request, account)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login!!')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('signup')

@login_required
def profile_view(request):
    return render(request, 'profile.html')