# Generated by Django 2.2.6 on 2019-11-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0005_answer_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='starred_answers',
            field=models.ManyToManyField(blank=True, related_name='answer_favs', to='question_box.Answer'),
        ),
        migrations.AddField(
            model_name='user',
            name='starred_questions',
            field=models.ManyToManyField(blank=True, related_name='question_favs', to='question_box.Question'),
        ),
    ]
