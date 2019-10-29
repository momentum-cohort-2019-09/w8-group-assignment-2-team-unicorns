from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    is_registered = models.BooleanField(default=False)
    

class Question(models.Model): 
    title = models.CharField(max_length=300, default=True)
    member = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="the_member", null=True) 
    tag = models.TextField()
   

class Answer(models.Model):
    title = models.CharField(max_length=300, default=True)
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, related_name="the_question", null=True) 
    answer = models.TextField()


