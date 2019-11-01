# Generated by Django 2.2.6 on 2019-11-01 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0003_auto_20191031_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]