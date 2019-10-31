from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from  question_box.forms import QuestionForm 
from django.db.models import Q

# Create your views here.

def home_page(request):
  all_question = Question.objects.all()
  search_term = request.GET.get('search')
  if search_term: 
    questions=questions.filter(
      Q(description__icontains=request.search_term) | 
      Q(title__icontains=request.search_term) |
      Q(author__icontains=request.search_term))

  return render(request, "question_box/home.html", {
    "all_question": all_question,
  })




  # if request.method =="POST":
  #   form = SearchForm(request.POST)
  #   if form.is_valid():
  #     search_word = form.cleaned_data['search_word'].lower()
  #     all_questions = all_questions.filter(title__icontains=search_word)
  # else:
  #   form = SearchForm()
  # return render(request, "question_box/home.html", {
  #   "question": all_questions,
  #   "form": form,
  # })

@login_required
def profile_page(request):
  user = request.user
  return render(request, "question_box/profile.html", {"user": user})

 