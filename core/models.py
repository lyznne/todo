
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=120, unique=True, null=False)
    bio = models.TextField(max_length=240)

    def __str__(self):
        return self.username
    
    
    
class Task(models.Model):
    task_name = models.CharField(max_length=120)
    task_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)  
    
    
    def __str__(self):
        return self.task_name
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=120)

    
    def __str__(self):
        return self.category_name