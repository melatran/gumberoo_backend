# Generated by Django 3.1.1 on 2020-09-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonstudent',
            name='mood',
            field=models.CharField(max_length=300),
        ),
    ]