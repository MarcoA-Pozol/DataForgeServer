from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_home, name='app-home'),
    path('import_export_data/', views.import_export_data, name='import-export-data'),
    path('data_visualization/', views.data_visualization, name='data-visualization'),
]