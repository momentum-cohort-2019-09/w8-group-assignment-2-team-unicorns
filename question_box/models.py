from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    member = models.BooleanField(default=False)
    questions = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, null=True)
    explanation = models.OneToManyField(to='Answer', on_delete=models.SET_NULL, blank=True, related_name="+")
    commentary = models.ManyToManyField(to='Comment', on_delete=models.SET_NULL, blank=True, related_name="+") 

class Question(models.Model): 
    question = models.CharField(max_length=300)
    description = models.TextField()
    tag = models.TextField()
    comments = models.ManyToManyField(to='Comment', related_name='+', blank=True)

class Answer(models.Model):
    answer = models.TextField()

class Comment(models.Model):
    comment = models.TextField()
    

