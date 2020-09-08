from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student
from api.models import Teacher
from api.serializers import TeacherSerializer


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

class StudentCreate():
  def get(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    for student in request.data[students]:
     teacher.student_set.create(first_name=student['first_name'], last_name=student['last_name'], age=student['age'])



