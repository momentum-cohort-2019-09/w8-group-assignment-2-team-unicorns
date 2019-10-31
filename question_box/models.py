from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    is_registered = models.BooleanField(default=False)
    

class Question(models.Model):  
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="questions", null=True)
    title = models.CharField(max_length=100) 
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
   

class Answer(models.Model):
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, related_name="answers", null=True) 
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="answers", null=True)
    title = models.CharField(max_length=300)
    answer = models.TextField()


