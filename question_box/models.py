from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_registered = models.BooleanField(default=False)

class Question(models.Model):
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="questions", null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_solved = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
   
class Answer(models.Model):
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, related_name="answers", null=True)
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="answers", null=True)
    answer = models.TextField()
    correct = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
 
    def __str__(self):
        return self.answer