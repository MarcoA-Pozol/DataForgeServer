from django.shortcuts import render, redirect

def app_home(request):
    return render(request, 'app_home.html')