from django.shortcuts import render, redirect

def app_home(request):
    return render(request, 'app_home.html')
    
def import_export_data(request):
    return render(request, 'import_export_data.html')