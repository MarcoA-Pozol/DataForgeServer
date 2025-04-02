from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view(), name='register-user'),
    path('logout/', views.LogoutAPIView.as_view(), name="logout-user"),
]