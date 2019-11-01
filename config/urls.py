"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from question_box import views

urlpatterns = [
   path('accounts/', include('registration.backends.default.urls')),
   path('', views.home_page, name='home_page'),
   path('accounts/home_logged_in/', views.home_logged_in, name='home_logged_in'),
   path('accounts/profile/', views.profile_page, name='profile_page'),
   path('question_box/<int:pk>/question_answers/',views.question_answers, name= 'question_answers'),
   path('admin/', admin.site.urls),
]


