# Generated by Django 3.1.1 on 2020-09-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonstudent',
            name='mood_analyzer',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]