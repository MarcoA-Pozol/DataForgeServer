from django.db import models
from Authentication.models import User

FILE_EXTENSION_CHOICES = ['csv', 'xls', 'xlsx', 'txt', 'pdf', 'json']
TIERS = ['Basic', 'Professional'] 
ALLOWED_FILES_TOTAL_SIZE = [1000, 100000] # MB (1G for basic tier, 100G for professional tier)
ALLOWED_DATABASE_QUERIES_PER_DAY = [50, 500] # Queries to the database
ALLOWED_API_REQUESTS_PER_DAY = [20, 300]

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_files') # User is the foreign key the file belongs to
    file = models.FileField(upload_to='userfiles/uploads/%Y/%m/%d/') # Store user files for each day for better control
    filename = models.CharField(max_length=255, null=False, unique=True) # This should manage in the data insertion layer to add the username to the filename first but showing it without the username in the name in the UI
    filetype = models.CharField(max_length=20, choices=FILE_EXTENSION_CHOICES, null=False) # Extensions like XLS, XLSX, JSON, CSV, SQL, etc. 
    filesize = models.IntegerField(null=False) # Add a validation layer for the filesize to allow only files under a determined size or weigth depending the tier the user haves
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Add a validation layer for data in formulary to ensure all fields are being filled
        
    def __str__(self):
        return f'{self.user.username} - {self.filename}'
        
class Tier(models.Model):
    name = models.CharField(max_length=20, choices=TIERS, null=False, default='Basic')
    allowed_files_total_size = models.IntegerField(choices=ALLOWED_FILES_TOTAL_SIZE, null=False, default=ALLOWED_FILES_TOTAL_SIZE[0])
    allowed_database_queries_per_day = models.IntegerField(choices=ALLOWED_DATABASE_QUERIES_PER_DAY, null=False, default=ALLOWED_DATABASE_QUERIES_PER_DAY[0])
    allowed_api_request_per_day = models.IntegerField(choices=ALLOWED_API_REQUESTS_PER_DAY, null=False, default=ALLOWED_API_REQUESTS_PER_DAY[0])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name