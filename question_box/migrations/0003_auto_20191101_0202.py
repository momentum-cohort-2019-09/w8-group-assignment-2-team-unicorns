# Generated by Django 2.2.6 on 2019-11-01 02:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0002_auto_20191031_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
