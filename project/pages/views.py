from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username = username,password = password)

    return render(request,'pages/about.html',{'loginform' : LoginForm})
