# Generated by Django 2.2.6 on 2019-11-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0002_auto_20191031_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
    ]
