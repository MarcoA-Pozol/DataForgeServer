from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from Authentication.models import User
from API.serializers import UserSerializer, UserUsernamesSerializer, UserAuthenticationSerializer
from abc import ABC, abstractmethod
import logging

# Logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# User viewset
class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for UserSerializer with caching.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 15))  # Cache responses for 15 minutes. This caches all requests, including GET, POST, PUT, and DELETE.
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    @method_decorator(cache_page(60 * 15)) # Cache the list retrieving for 15 minutes.
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserUsernamesAPIView(APIView):
    """
    Custom API view to expose only usernames.
    This endpoint is open to anyone, their main purpose is to be called on the Client side on the React App.
    """
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Rate limiting
    pagination_class = PageNumberPagination  # Enable pagination

    @method_decorator(cache_page(60 * 15))  # Cache entire view for 15 minutes
    def get(self, request):
        query = request.GET.get('username', '')  # Get 'username' query param
        cache_key = f"cached_users_{query}"  # Unique cache key per query
        
        # Check if cached data exists
        users = cache.get(cache_key)
        if users is None:
            print(f"Cache miss for key: {cache_key}")
            # Convert QuerySet to list of dictionaries before caching
            users = list(User.objects.filter(username__icontains=query).values("id", "username"))
            cache.set(cache_key, users, timeout=60 * 15)  # Store serialized data in cache
        else:
            print(f"Cache hit for key: {cache_key}")

        paginator = self.pagination_class()
        paginated_users = paginator.paginate_queryset(users, request)  # Pass list, not QuerySet
        serializer = UserUsernamesSerializer(paginated_users, many=True)
        response = paginator.get_paginated_response(serializer.data)

        return response

# Users authentication endpoint.
class I_AuthenticationAPIView(ABC):
    def get(self, request):
        pass
        
    def post(self, request):
        pass
        
class UserAuthenticationDataAPIView(APIView, I_AuthenticationAPIView):
    """
    Expose user´s authentication process required data(username, password, email, etc).
    """
    def get(self, request):
        """
        Check if an user exists in cache or database.
        """
        query = request.GET.get('username', 'password') # Query parameters (?username=&password=)
        cache_key = f'cached_users_{query}' # Cached key for the requested user
        
        # Check if requested user in cache
        user = cache.get(cache_key)
        if user is None: # Obtaining user from database
            logging.warning(f'Cache miss for key: {cache_key}')
            data = User.objects.get(username=request.GET.get('username'), password=request.GET.get('password'))
            serializer = UserAuthenticationSerializer(data, many=True)
            response = serializer.data
        else: # Obtaining user from cache
            logging.info(f'Cahe key was obtained: {cache_key}')
            response = user
        
        return response