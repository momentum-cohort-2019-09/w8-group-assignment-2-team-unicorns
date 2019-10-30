from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question_box.models import User, Question, Answer
from question_box.forms import SearchForm

# Create your views here.

def profile_page(request):
  page = request.page
  return render(request, "question_box/profile.html", {"page": page})

@login_required
def login_view(request): 
    user = request.user
    return render(request, "question_box/home.html", {"user": user})

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
