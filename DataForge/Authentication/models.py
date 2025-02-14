from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        User Model to save User instances as rows in the DB
    """
    is_superuser = models.BooleanField(default=False, null=False)
    country = models.CharField(max_length=200, null=False, unique=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, unique=False)

    def __str__(self):
        return self.username