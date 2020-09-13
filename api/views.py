import json
from django.http import JsonResponse, QueryDict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db.models import Avg

from api.models import Teacher, Lesson, LessonStudent, Student
from api.popos import StudentScore, LessonScore
from api.serializers import TeacherSerializer, LessonSerializer, LessonStudentSerializer, StudentSerializer, StudentScoreSerializer, LessonScoreSerializer


class TeacherList(generics.CreateAPIView, generics.ListAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveAPIView):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer


class TeacherStudent(APIView):
  parser_classes=[JSONParser]

  def get(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return Response(StudentSerializer(teacher.student_set, many=True).data)

  def post(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    students = []

    for student in request.data['students']:
      students.append(teacher.student_set.create(first_name=student['first_name'], last_name=student['last_name']))
    
    return Response(StudentSerializer(students, many=True).data)


class LessonDetail(APIView):
  parser_classes = [JSONParser]

  def get(self, request, pk):
    lesson = Lesson.objects.get(pk=pk)
    return Response(LessonSerializer(lesson).data)

    
class TeacherLesson(APIView):
  parser_classes = [JSONParser]

  def get(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    lessons = teacher.lesson_set.all()
    
    return Response(LessonSerializer(lessons, many=True).data)

  def post(self, request, pk):
    teacher = Teacher.objects.get(pk=pk)
    new_lesson = teacher.lesson_set.create(name=request.data['lesson']['name'])

    for question in request.data['lesson']['questions']:
      new_question = new_lesson.question_set.create(
        question=question['question'],
        reading=question['reading']
      )
      for answer in question['answers']:
        new_question.answer_set.create(
          answer=answer['answer'],
          correct=json.loads(answer['correct'].lower())
        )

    return Response(LessonSerializer(new_lesson).data, status=201)


class LessonStudentDetail(APIView):
  parser_classes = [JSONParser]
  
  def post(self, request, pk):
    student = Student.objects.get(pk=pk)
    new_lessonstudent = student.lessonstudent_set.create(
      lesson_id=request.data['lesson'],
      score=request.data['score'],
      mood=request.data['mood']
    )

    return Response(LessonStudentSerializer(new_lessonstudent).data)


class StudentAverage(APIView):
  parser_classes = [JSONParser]

  def get(self, request, pk):
    average_score = LessonStudent.student_average_score(pk)['score__avg']
    student_score = StudentScore(student_id=pk, average_score=average_score)
    
    return Response(StudentScoreSerializer(student_score).data)


class LessonAverage(APIView):
  parser_classes = [JSONParser]

  def get(self, request, pk):
    average_score = LessonStudent.lesson_average_score(pk)['score__avg']
    lesson_score = LessonScore(lesson_id=pk, average_score=average_score)
    
    return Response(LessonScoreSerializer(lesson_score).data)
