from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from  question_box.forms import SearchForm

# Create your views here.

def profile_page(request):
  page = request.page
  return render(request, "question_box/profile.html", {"page": page})
  
@login_required
def login_view(request): 
    user = request.user
    return render(request, "question_box/profile.html", {"user": user})



def questions(request):
    allquestions = Question.objects.filter(author=request.user)
    if request.method =="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()

            return redirect(to='profile')
    else:
        form = QuestionForm()

    return render(request, "question_box/questions.html", {"form": form}) 

def question_answers(request):
    allanswers = Answer.objects.all()
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = form.save()

            return redirect(to='question_answers')
    else:
        form = QuestionForm()

    return render(request, "question_box/question_answers.html", {"form": form}) 

     

def question_answers(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, "question_box/question_answers.html",
                  {"question": question}) 
        

# def home(request): 
#     all_questions = Question.objects.all()
#     if request.method =="POST":
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             search_word = form.cleaned_data['search_word'].lower()
#             all_questions = all_questions.filter(title__icontains=search_word)
#     else:
#         form = SearchForm()
#     return render(request, "question_box/home.html", {
#         "question": all_questions,
#         "form": form,
#     })
