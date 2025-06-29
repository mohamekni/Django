from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def about(request):

    if request.method == 'POST':
        dataForm = LoginForm(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # data = Login(username = username,password = password)
    # data.save()

    return render(request,'pages/about.html',{'loginform' : LoginForm})
