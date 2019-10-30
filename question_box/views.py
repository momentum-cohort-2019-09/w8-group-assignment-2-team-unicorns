from django.shortcuts import render

# Create your views here.

def profile_page(request):
  page = request.page
  return render(request, "question_box/profile.html", {"page": page})
