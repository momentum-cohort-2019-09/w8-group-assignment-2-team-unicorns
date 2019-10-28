from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    member = models.BooleanField(default=False)
    questions = models.ForeignKey(to='Question', on_delete=models.SET_NULL, blank=True, null=True)

class Question(models.Model): 
    question = models.CharField(max_length=255)

class Answer(models.Model):
    pass

class Comments(models.Model):
    pass