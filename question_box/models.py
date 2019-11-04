from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    starred_questions = models.ManyToManyField(to='Question', related_name="question_favs", blank=True)
    starred_answers = models.ManyToManyField(to='Answer', related_name="answer_favs", blank=True)

class Question(models.Model):
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="questions", null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
   
class Answer(models.Model):
   question = models.ForeignKey(to='Question', on_delete=models.CASCADE, blank=True, related_name="answers", null=True)
   author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="answers", null=True)
   answer = models.TextField()
   correct = models.BooleanField()

   def __str__(self):
       return self.answer

    # you’ll need to make migrations
    # then I opened a new file inside static as index.js
    # document.querySelector(‘#correct-answer’).addEventListener(‘click’, function (event) {
#    const el = event.target
#    console.log({ el })
#    const answerId = el.dataset.answerid
#    fetch(/question_box/${answerid}/mark_correct/, {
#        method: ‘POST’
#    }).then(res => {
#        if (res.correct) {
#            console.log(‘correct’)
#            // el.classList.toggle(‘fas’)
#            // el.classList.toggle(‘’)
#        }
#    })
