from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='thumbnails')
    description = models.CharField(max_length=5000)
    
# Create your models here.
