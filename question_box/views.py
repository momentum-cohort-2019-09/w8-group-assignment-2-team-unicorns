from django.shortcuts import render, redirect
from question_box.models import User, Question, Answer
from  question_box.forms import SearchForm

# Create your views here.
def home(request): 
    all_questions = Question.objects.all()
    if request.method =="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data['search_word'].lower()
            all_questions = all_questions.filter(title__icontains=search_word)
    else:
        form = SearchForm()
    return render(request, "question_box/home.html", {
        "question": all_questions,
        "form": form,
    })