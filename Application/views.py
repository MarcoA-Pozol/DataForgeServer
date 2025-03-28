from django.shortcuts import render
from . tasks import retrieve_current_user_data
import threading

def app_home(request):
    if request.user.is_authenticated:
        return render(request, 'app_home.html')
    return None

def import_export_data(request):
    return None

def data_visualization(request):
    return None

def user_data_view(request):
    auth_user = request.user

    # Execute second plane task when button is clicked on FrontEnd
    if request.method == "GET":
        threading.Thread(target=retrieve_current_user_data, args=[auth_user,]).start()

    return None