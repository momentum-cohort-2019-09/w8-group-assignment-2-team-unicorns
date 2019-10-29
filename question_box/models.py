from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    member = models.BooleanField(default=False)

class Question(models.Model): 
    title = models.CharField(max_length=300, default=True)
    tag = models.TextField()
    member = models.ForeignKey(to='Member', on_delete=models.SET_NULL, blank=True, related_name="the_member", null=True) 
   

class Answer(models.Model):
    title = models.CharField(max_length=300, default=True)
    answer = models.TextField()
    question = models.ForeignKey(to='Question', on_delete=models.SET_NULL, blank=True, related_name="the_question", null=True) 
    

class Comment(models.Model):
    comment = models.TextField(max_length=300, default=True)
    answer = models.ForeignKey(to='Answer', on_delete=models.SET_NULL, blank=True, related_name="question_answer", null=True)
    

