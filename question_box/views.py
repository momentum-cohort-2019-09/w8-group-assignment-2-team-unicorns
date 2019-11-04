from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from question_box.models import User, Question, Answer
from question_box.forms import QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
    
def mark_correct(request, pk):
    answer = Answer.objects.get(pk=pk)
    if not answer.correct:
      answer.correct = True
      return JsonResponse({"correct": True })

@login_required
@csrf_exempt
def toggle_favorite_question(request, pk):
  question = get_object_or_404(Question, pk=pk)
  if question in request.user.starred_questions.all():
    request.user.starred_questions.remove(question)
    is_favorite = False
  else:
    request.user.starred_questions.add(question)
    is_favorite = True
  return JsonResponse({"ok": True, "is_favorite": is_favorite})

