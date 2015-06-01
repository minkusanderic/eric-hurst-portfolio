from django.db import models

class Education(models.Model):
    grad_date = models.DateField("Graduation Date")
    school = models.CharField(max_length=200)
    gpa = models.CharField(max_length=4)
    
# Create your models here.
