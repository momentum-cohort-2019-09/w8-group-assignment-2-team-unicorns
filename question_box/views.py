from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from question_box.forms import QuestionForm, AnswerForm

def home_page(request):
  user = request.user
  return render(request, "question_box/home.html", {"user": user})

@login_required
def profile_page(request):
  user = request.user
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
      question = form.save(commit=False)
      question.author = user
      question = form.save()

      return redirect(to='profile_page')   
  else:
    form = QuestionForm()
      
  return render(request, "question_box/profile.html", {"user": user, "form": form})

@login_required
def home_logged_in(request): 
  questions = Question.objects.all()
  return render(request, "question_box/home_logged_in.html", {"questions": questions})


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

@login_required 
def question_answers(request, pk): 
  question = Question.objects.get(pk=pk)
  allanswers = question.answers.all()
  if request.method =="POST":
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.author = request.user
      answer.question = question
      answer.save()
      return redirect(to='question_answers', pk=pk)
  else:
    form = AnswerForm()
    return render(request, "question_box/question_answers.html", {"question": question, "answers": allanswers, "form": form})

