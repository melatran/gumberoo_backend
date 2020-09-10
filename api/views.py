from django.http import JsonResponse, QueryDict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api.models import Teacher, Lesson
from api.serializers import TeacherSerializer, LessonSerializer


class TeacherList(generics.CreateAPIView, generics.ListAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

  
class TeacherDetail(generics.RetrieveAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer


class TeacherLesson(APIView):
  parser_classes = [JSONParser]

  def post(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    new_lesson = teacher.lesson_set.create(name=request.data['lesson']['name'])

    for question in request.data['lesson']['questions']:
      new_question = new_lesson.question_set.create(
        question=question['desc'],
        reading=question['reading']
      )
      for answer in question['answers']:
        new_question.answer_set.create(
          answer=answer['desc'],
          correct=answer['correct']
        )

    return Response(LessonSerializer(new_lesson).data, status=201)

  def get(self, request, pk1, pk2):
    lesson = Lesson.objects.get(pk=pk2)
    return Response(LessonSerializer(lesson).data)