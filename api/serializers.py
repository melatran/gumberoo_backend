from rest_framework import serializers

from api.models import Teacher
from api.models import Student

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = (
      'id', 'first_name', 'last_name'
    )

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = (
        'teacher', 'id', 'first_name', 'last_name', 'age'
    )
