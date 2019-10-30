# Generated by Django 2.2.6 on 2019-10-29 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='member',
            new_name='is_registered',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.RemoveField(
            model_name='user',
            name='questions',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_question', to='question_box.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='title',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
