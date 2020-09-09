from rest_framework import serializers

from api.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = (
      'id', 'first_name', 'last_name'
    )

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = (
      'id', 'first_name', 'last_name'
    )