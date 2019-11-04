

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0004_auto_20191101_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
