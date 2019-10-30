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
<<<<<<< HEAD
    path('', views.login_view, name='home'), 
=======
    path('', views.home_view, name='home'), 
    path('/profile/', views.profile_page, name='profile'),
>>>>>>> 0fff3da12d08ad42783ddac3c52dca4b69a4e87b
    path('admin/', admin.site.urls),
]
