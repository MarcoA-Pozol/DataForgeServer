from rest_framework import serializers
from Authentication.models import User

class UserSerializer(serializers.ModelSerializer):
	"""
		Serializer for User model.
		Fields will be showed in the response (Do not expose confidential data).
	"""
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'country', 'language']
		# fields = '__all__'
		

class UserUsernamesSerializer(serializers.ModelSerializer):
	"""
		Serializer for User model that exposes only the usernames in the response,
		thought to be user by GET request.
	"""
	class Meta:
		model = User
		fields = ['username', 'country', 'language']