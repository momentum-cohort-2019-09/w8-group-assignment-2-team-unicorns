from django import forms
from question_box.models import Question
from django.forms import ModelForm

class QuestionForm(forms.ModelForm):
  
  class Meta:
    model = Question
    fields = ['title','description']
  