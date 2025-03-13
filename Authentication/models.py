from django.db import models
from django.contrib.auth.models import AbstractUser
from . datasets import COUNTRY_CHOICES, LANGUAGE_CHOICES
from django.core.cache import cache


class User(AbstractUser):
    """
        User Model to save User instances as rows in the DB
    """
    is_superuser = models.BooleanField(default=False, null=False)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='US', null=False, unique=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en', unique=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, unique=False, default="profile_pictures/default_profile_picture.jpg")

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete_pattern("cached_users_*")  # Clear user cache

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        cache.delete_pattern("cached_users_*")  # Clear user cache