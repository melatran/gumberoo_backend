import json
from django.http import JsonResponse, QueryDict
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.models import Student
from api.models import Teacher
from api.serializers import TeacherSerializer, StudentSerializer


class TeacherList(generics.CreateAPIView, generics.ListAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

  
class TeacherDetail(generics.RetrieveAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

  # def get(self, request, pk):
  #   teacher = Teacher.objects.get(pk=pk)

  #   serializer = TeacherSerializer(teacher)
  #   return Response(serializer.data)


class TeacherStudent(APIView):
  parser_classes=[JSONParser]

  def get(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return Response(StudentSerializer(teacher.student_set, many=True).data)
    

  def post(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    students = []
    for student in request.data['students']:
      students.append(teacher.student_set.create(first_name=student['first_name'], last_name=student['last_name'], age=student['age']))
    return Response(StudentSerializer(students, many=True).data)
