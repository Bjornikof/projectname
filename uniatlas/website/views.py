from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'website/home.html')


def resultpage(request):
    return render(request, 'website/resultpage.html')


def login(request):
    return render(request, 'website/login.html')


def signup(request):
    return render(request, 'website/signup.html')


def unisozluk(request):
    return render(request, 'website/unisozluk.html')


def unipage(request):
    return render(request, 'website/unipage.html')

def uniedit(request):
    return render(request, 'website/uniedit.html')


def profile(request):
    return render(request, 'website/profile.html')


def unilist(request):
    return render(request, 'website/unilist.html')


def assistant(request):
    return render(request, 'website/assistant.html')


def userprofile(request):
    return render(request, 'website/userprofile.html')
