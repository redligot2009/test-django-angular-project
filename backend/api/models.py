from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    pass

class TodoList(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE, null=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=255,default="New List")
    description = models.CharField(max_length=255,default="Insert your list's description here.")

    def __str__(self):
        return 


class TodoItem(models.Model):
    
    list = models.ForeignKey(to=TodoList,on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255,default="New Item")
    description = models.TextField(default="Insert your description here.")
    finished = models.BooleanField(default=False)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
