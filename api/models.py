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
  age = models.IntegerField
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)