from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from question_box.forms import QuestionForm, AnswerForm

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

@login_required
def profile_page(request):
 user = request.user
 return render(request, "question_box/profile.html", {"user": user})

def question_create(request):
 if request.method == 'POST':
   form = QuestionForm(request.POST)
   if form.is_valid():
     question = form.save()
     return redirect(to=profile_page)
 else:
   form = QuestionForm()
 return render(request, "question_box/profile.html", {"form": form})

def question_render(request, pk):
 allquestions = Question.objects.filter(author=request.user)
 if request.method =="POST":
     form = QuestionForm(request.POST)
     if form.is_valid():
         question = form.save()
         return redirect(to='profile', pk=allquestions.pk)
 else:
     form = QuestionForm()
 return render(request, "question_box/profile.html", {"form": form})


def question_answers(request, pk): 
  allanswers = Answer.objects.filter(question_id=pk)
  if request.method =="POST":
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save()
      return render(request, "question_box/question_answers.html", {"form": form})
  else:
    form = AnswerForm()
  return render(request, "question_box/question_answers.html", {"form": form})


def add_answers(request, pk):
  if request.method == "POST":  
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save()
      return render(request, "question_box/question_answers.html", {"form": form})
  else:
    form = AnswerForm()
  return render(request, "question_box/question_answers.html", {"form": form})