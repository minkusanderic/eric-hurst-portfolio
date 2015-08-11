from django.db import models

# Create your models here.

class Message(models.Model):
   from_email = models.CharField(max_length=500)
   msg = models.CharField(max_length=5000) 
 
   def __unicode__(self):
       return "Message from " + from_email
