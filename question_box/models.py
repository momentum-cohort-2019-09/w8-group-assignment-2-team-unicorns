from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    member = models.BooleanField(default=False)
    questions = models.ManyToManyField(to='Question', 
                                  on_delete=models.CASCADE, 
                                  blank=True, null=True)
    answers = models.ForeignKey(to='Answer', 
                                    on_delete=models.SET_NULL, 
                                    blank=True, 
                                    related_name=answer)
    comments = models.ForeignKey(to='Comment', on_delete=models.SET_NULL, blank=True, related_name=comment)

class Question(models.Model): 
    question = models.CharField(max_length=255)
    answers = models.ManyToManyField(to='Answer', on_delete=models.SET_NULL, blank=True, related_name=answers)

class Answer(models.Model):
    answers = models.CharField(max_length=255)
     
    comments = models.ManyToManyField(to='Comment', on_delete=models.SET_NULL, blank=True, related_name=comment)

class Comment(models.Model):
    comments = models.CharField(max_length=300)
    answers = models.ForeignKey(to='Answer', on_delete=models.SET_NULL, blank=True, related_name=answers)

    
