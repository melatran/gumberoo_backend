from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Teacher
from api.serializers import TeacherSerializer

class TeacherList(generics.ListAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  
