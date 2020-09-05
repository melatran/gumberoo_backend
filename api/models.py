from django.db import models

# Create your models here.

class Teacher(models.Model):
  first_name = models.CharField
  last_name = models.CharField
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
