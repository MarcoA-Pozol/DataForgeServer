from django.shortcuts import render, redirect

def app_home(request):
    if request.user.is_authenticated:
        return render(request, 'app_home.html')
    return redirect('authentication')

def import_export_data(request):
    return render(request, 'import_export_data.html')

def data_visualization(request):
    return render(request, 'app_data_visualization.html')