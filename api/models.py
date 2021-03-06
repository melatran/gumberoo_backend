from django.db import models
from django.db.models import Avg

class Teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.full_name()

  def full_name(self):
    return str(f'{self.first_name} {self.last_name}')

class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.full_name()

  def full_name(self):
    return str(f'{self.first_name} {self.last_name}')

class Lesson(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  students = models.ManyToManyField(Student, through='LessonStudent', through_fields=('lesson', 'student'),)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class LessonStudent(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  score = models.IntegerField()
  mood = models.CharField(max_length=300)
  mood_analyzer = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def student_average_score(student_id):
    score = LessonStudent.objects.filter(student_id=student_id).aggregate(Avg('score'))
    return score

  def lesson_average_score(lesson_id):
    score = LessonStudent.objects.filter(lesson_id=lesson_id).aggregate(Avg('score'))
    return score

class Question(models.Model):
  question = models.CharField(max_length=100)
  reading = models.CharField(max_length=250)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.question
    
class Answer(models.Model):
  answer = models.CharField(max_length=100)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.answer
