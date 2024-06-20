from django.shortcuts import redirect, render

# Create your views here.

def index (request):
    return redirect('account_login')

def home (request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre-nos.html')
