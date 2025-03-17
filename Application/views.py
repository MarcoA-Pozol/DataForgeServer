from django.shortcuts import render, redirect
from . tasks import retrieve_current_user_data
import threading

def app_home(request):
    if request.user.is_authenticated:
        return render(request, 'app_home.html')
    return redirect('authentication')

def import_export_data(request):
    return render(request, 'import_export_data.html')

def data_visualization(request):
    return render(request, 'app_data_visualization.html')

def user_data_view(request):
    auth_user = request.user

    # Execute second plane task when button is clicked on FrontEnd
    if request.method == "GET":
        threading.Thread(target=retrieve_current_user_data, args=[auth_user,]).start()

    return render(request, 'user_data.html')