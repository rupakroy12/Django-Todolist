from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone

# import datetime

# Create your models here.

class Task(models.Model):
    
    title = models.CharField(max_length= 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    deleted = models.DateTimeField(auto_now_add = True)


    def __str__ (self):
        return self.title
