from django import forms
from question_box.models import Question, Answer
from django.forms import ModelForm

class QuestionForm(forms.ModelForm):

 class Meta:
   model = Question
   fields = ['title','description']

class AnswerForm(forms.ModelForm):

 class Meta:
   model = Answer
   fields = ['answer']