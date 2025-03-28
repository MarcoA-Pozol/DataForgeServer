from rest_framework import serializers
from Authentication.models import User

class UserSerializer(serializers.ModelSerializer):
	"""
		Serializer for User model.
		Fields will be showed in the response (Do not expose confidential data).
	"""
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'country', 'language', 'profile_picture']
		# fields = '__all__'
		

class UserUsernamesSerializer(serializers.ModelSerializer):
	"""
		Serializer for User model that exposes only the usernames in the response,
		thought to be user by GET request.
	"""
	class Meta:
		model = User
		fields = ['username', 'country', 'language']


class UserAuthenticationSerializer(serializers.ModelSerializer):
    """
        Serializer for User model that exposes username and password(encrypted) in the response for the authentication process wether registering or login.
    """
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisteringSerializer(serializers.ModelSerializer):
	"""
		Serializer for User registering process for new account creation.
	"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'country', 'profile_picture']