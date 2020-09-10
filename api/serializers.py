from rest_framework import serializers
from api.models import Teacher, LessonStudent

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = (
      'id', 'first_name', 'last_name'
    )

class LessonStudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = LessonStudent
    fields = (
      "student", "lesson", "score", "mood"
    )