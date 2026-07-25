from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    # http://127.0.0.1:8000/ will always redirect to http://127.0.0.1:8000/login/
    return redirect('login:login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            # Renders the same template but provides an error message as context
            return render(request, 'login/index.html', {'error_message': 'Invalid username or password. Please try again.'})

    return render(request, 'login/index.html')


def user_logout(request):
    logout(request)

    # For users to sign in again
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, 'login/index.html', {'error_message': 'Invalid username or password. Please try again.'})

    return render(request, 'login/index.html')


def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'login/signup.html', {'form': form})