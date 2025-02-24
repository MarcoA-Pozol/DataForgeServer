from django.db import models
from django.contrib.auth.models import AbstractUser
from . datasets import COUNTRY_CHOICES, LANGUAGE_CHOICES


class User(AbstractUser):
    """
        User Model to save User instances as rows in the DB
    """
    is_superuser = models.BooleanField(default=False, null=False)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='US', null=False, unique=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en', unique=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, unique=False, default="img/default_profile_picture.jpg")

    def __str__(self):
        return self.username