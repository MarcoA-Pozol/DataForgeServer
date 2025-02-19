from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('Authentication.urls')),
    path('app/', include('Application.urls')),
]
