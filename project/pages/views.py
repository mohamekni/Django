from django.shortcuts import render


# Create your views here.

def index(request):
    myInfo = {
        'firstName':'Moha So Good No Love',
        'lastName':'LaSquale',
        'age':23,
        'fileSize':200000000
    }
    return render(request,'pages/index.html', myInfo)

def about(request):
    return render(request,'pages/about.html')
