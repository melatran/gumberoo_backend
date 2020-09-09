from rest_framework import serializers

from api.models import Teacher, Lesson, Question, Answer

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = (
      'id', 'first_name', 'last_name'
    )

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = (
      'id', 'answer', 'correct'
    )
    depth = 0

class QuestionSerializer(serializers.ModelSerializer):
  answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Question
    fields = (
      'id', 'question', 'reading', 'answers'
    )
    read_only_fields = (
      'answers'
    )

class QuestionAnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    depth = 1
    fields = ('id', 'answer', 'correct')

class LessonQuestionSerializer(serializers.ModelSerializer):
  answers = QuestionAnswerSerializer(source='answer_set', many=True, read_only=True)
  class Meta:
    model = Question
    depth = 1
    fields = ('id', 'question', 'reading', 'answers')

class LessonSerializer(serializers.ModelSerializer):
  questions = LessonQuestionSerializer(source='question_set', many=True, read_only=True)
  class Meta:
    model = Lesson
    fields = (
      'id', 'name', 'questions'
    )
    read_only_fields = ['questions']
    depth = 1

