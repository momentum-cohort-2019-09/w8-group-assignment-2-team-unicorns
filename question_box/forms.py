from django import forms
from question_box.models import Question
from django.forms import ModelForm

class QuestionForm(forms.ModelForm):
  
  class Meta:
    model = Question
    fields = ['question']
  
class SearchForm(forms.Form):
  search_word = forms.CharField(label="Search", max_length=100)
