from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    member = models.BooleanField(default=False)
    questions = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, null=True)
    answers = models.OneToManyField(to='Answer', on_delete=models.SET_NULL, blank=True, related_name=answer)
    comments = models.ManyToManyField(to='Comment', on_delete=models.SET_NULL, blank=True, related_name=comment)

class Question(models.Model): 
    question = models.CharField(max_length=255)

class Answer(models.Model):
    answer = models.CharField(max_length=255)
    description = models.TextField()   
    comments = models.ManyToManyField(to='Comment', on_delete=models.SET_NULL, blank=True, related_name=commen


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    description = models.TextField()

    