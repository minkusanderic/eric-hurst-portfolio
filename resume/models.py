from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    gpa = models.CharField(max_length=4)
    grad_date = models.DateField("Graduation Date")

    def __unicode__(self):
        return self.school

class Class(models.Model):
    school = models.ForeignKey(Education)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.name
# Create your models here.
