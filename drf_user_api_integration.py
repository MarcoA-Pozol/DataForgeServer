"""serializers/user_serializers.py"""
from rest_framework import serializers
from Authentication.models import User

# User serializer
class UserSerializer(serializer.ModelSerializer):
	"""
		Serializer for User model.
	"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'country']
		# fields = '__all__'
		

"""views/user_views.py"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Authentication.models import User
from . serializers.user_serializers import UserSerializer

# User viewset
class UserViewSet(viewsets.ModelViewSet):
	"""
		Viewset for UserSerializer.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    

"""urls.py"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views.user_views import UserViewSet
from rest_framework.simple_jwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet, 'api-users')
# router.register('path', AnotherViewSet, 'path-name')
# router.register('path', AnotherViewSet, 'path-name')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]


"""React connection settings"""
# Install with "pip install django-cors-headers" for a React app connection if it's on a different origin.