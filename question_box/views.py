from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from question_box.forms import QuestionForm, AnswerForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
def home_page(request):
  user = request.user
  return render(request, "question_box/home.html", {"user": user})


@csrf_exempt
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
  
@csrf_exempt
@login_required
def home_logged_in(request): 
  questions = Question.objects.all()
  return render(request, "question_box/home_logged_in.html", {"questions": questions})

@csrf_exempt
def question_create(request):
 if request.method == 'POST':
   form = QuestionForm(request.POST)
   if form.is_valid():
     question = form.save()
     return redirect(to='profile_page')
 else:
   form = QuestionForm()
 return render(request, "question_box/profile.html", {"form": form})

@csrf_exempt
def question_render(request, pk):
 allquestions = Question.objects.filter(author=request.user)
 if request.method =="POST":
     form = QuestionForm(request.POST)
     if form.is_valid():
         question = form.save()
         return redirect(to='profile_page', pk=allquestions.pk)
 else:
     form = QuestionForm()
 return render(request, "question_box/profile.html", {"form": form})

@csrf_exempt
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

def delete_answer(request, pk):
    answer = get_object_or_404(Note, pk=pk)         
    if request.method == "POST":
        answer.delete()
        return redirect(to='question_answers')

    return render(request, 'question_box/question_answers.html', {"answer":answer}) 

@csrf_exempt
def mark_correct(request, pk):
    answer = Answer.objects.get(pk=pk)
    question = answer.question
    answer.correct = True
    answer.question.is_solved = True
    answer.save()
    answer.question.save()
    return JsonResponse({"correct": True })




