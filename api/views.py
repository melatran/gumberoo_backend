from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api.models import Teacher, LessonStudent, Student
from api.serializers import TeacherSerializer, LessonStudentSerializer
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
class LessonStudent(APIView):
  parser_classes = [JSONParser]
  
  def post(self, request, pk):
    student = Student.objects.get(pk=pk)
    new_lessonstudent = student.lessonstudent_set.create(
      lesson_id=request.data['lesson'],
      score=request.data['score'],
      mood=request.data['mood']
    )

    return Response(LessonStudentSerializer(new_lessonstudent).data)
