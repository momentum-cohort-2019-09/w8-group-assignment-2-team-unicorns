from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from question_box.models import User, Question, Answer
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)