from django.db import models

# Create your models here.

class Teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField()
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  students = models.ManyToManyField(Student, through='LessonStudent', through_fields=('lesson', 'student'),)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
class LessonStudent(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  score = models.IntegerField()
  mood = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
  question = models.CharField(max_length=100)
  reading = models.CharField(max_length=250)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
  answer = models.CharField(max_length=100)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
