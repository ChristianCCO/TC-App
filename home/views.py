from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # http://127.0.0.1:8000/home/ will redirect to login if user is not authenticated
        return redirect('login:index')
    else:
        return render(request, 'home/index.html')