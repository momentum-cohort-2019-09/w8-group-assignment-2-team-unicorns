from django import forms
from question_box.models import Question, Answer
from django.forms import ModelForm


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','description']

class SearchForm(forms.Form):
    search_word = forms.CharField(label="Search", max_length=100)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

