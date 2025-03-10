from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from Authentication.models import User
from API.serializers.user_serializers import UserSerializer, UserUsernamesSerializer

# User viewset
class UserViewSet(viewsets.ModelViewSet):
	"""
		Viewset for UserSerializer.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

class UserUsernamesAPIView(APIView):
    """
    Custom API view to expose only usernames.
    This endpoint is open to anyone, their main purposse is to be called on the Client side on the React App.
    """
    permission_classes = [AllowAny] 
    throttle_classes = [AnonRateThrottle, UserRateThrottle] # Throttling for rate limiting (Modify rate/timeframe in settings.py (REST_FRAMEWORK)).
    pagination_class = PageNumberPagination # Add pagination

    def get(self, request):
        query = request.GET.get('username', '') # Filter by 'username' using an url query(Let in blank to retrieve all ('' by default for all)).
        users = User.objects.filter(username__icontains=query) # Retrieve whoever user containing the provided in query second parameter value in their username value.
        paginator = self.pagination_class()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = UserUsernamesSerializer(paginated_users, many=True)
        response = paginator.get_paginated_response(serializer.data) # Get desired page using '?page=<page_number>' in the url query. Let in blank to retrieve the first 10 for the first page.

        return response