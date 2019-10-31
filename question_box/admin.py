from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from question_box.models import User, Question, Answer


class QuestionAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'description',
    'created_at',
    'updated_at',
  )


admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)