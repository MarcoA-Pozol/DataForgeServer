from django.db import models
from Authentication.models import User

FILE_EXTENSION_CHOICES = ['csv', 'xls', 'xlsx', 'txt', 'pdf', 'json']

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_files') # User is the foreign key the file belongs to
    file = models.FileField(upload_to='userfiles/uploads/%Y/%m/%d/') # Store user files for each day for better control
    filename = models.CharField(max_length=255, null=False, unique=True) # This should manage in the data insertion layer to add the username to the filename first but showing it without the username in the name in the UI
    filetype = models.CharField(max_length=20, choices=FILE_EXTENSION_CHOICES, null=False) # Extensions like XLS, XLSX, JSON, CSV, SQL, etc. 
    filesize = models.IntegerField(null=False) # Add a validation layer for the filesize to allow only files under a determined size or weigth depending the tier the user haves
    