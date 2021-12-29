from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=50, null=True)
    desc = models.TextField(null=True)
    details = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    