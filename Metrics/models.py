from django.db import models
from Authentication.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_logs')
    detail = models.TextField(null=False)
    tag = models.CharField(max_length=30, null=False, default='Not Specified')
    datetime= model.DateTime(auto_now_add=True)
    
    def __str__(self):
        return self.detail