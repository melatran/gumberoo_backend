from django.test import TestCase
from api.models import Teacher, Student, Lesson, Question, Answer

class TeacherModelTest(TestCase):
  def setUp(self):
    teacher = Teacher.objects.create(first_name='teacher1First', last_name='teacher1Last')

  def test_string_representation(self):
    teacher = Teacher.objects.get(first_name='teacher1First')
    self.assertEqual(str(teacher), teacher.full_name())

  def test_full_name(self):
    teacher = Teacher.objects.get(first_name='teacher1First')
    self.assertEqual(str(teacher.full_name()), str(f'{teacher.first_name} {teacher.last_name}'))

class StudentModelTest(TestCase):
  def setUp(self):
    teacher = Teacher.objects.create(first_name='teacher2First', last_name='teacher2Last')
    teacher.student_set.create(first_name='student2First', last_name='student2Last', age=6)

  def test_string_representations(self):
    student = Student.objects.get(first_name='student2First')
    self.assertEqual(str(student), student.full_name())

  def test_full_name(self):
    student = Student.objects.get(first_name='student2First')
    self.assertEqual(str(student.full_name()), str(f'{student.first_name} {student.last_name}'))

class LessonModelTest(TestCase):
  def setUp(self):
    Lesson.objects.create(name='lesson1', description='lesson1 Description')

  def test_string_representation(self):
    lesson = Lesson.objects.get(name='lesson1')
    self.assertEqual(str(lesson), lesson.name)

class QuestionModelTest(TestCase):
  def setUp(self):
    lesson = Lesson.objects.create(name='lesson2', description='lesson2 Description')
    lesson.question_set.create(question='question1', reading='question1 Reading')

  def test_string_representation(self):
    question = Question.objects.get(question='question1')
    self.assertEqual(str(question), question.question)

class AnswerModelTest(TestCase):
  def setUp(self):
    lesson = Lesson.objects.create(name='lesson3', description='lesson3 Description')
    question = lesson.question_set.create(question='question2', reading='question2 Reading')
    question.answer_set.create(answer='answer1', correct=False)
  
  def test_string_representation(self):
    answer = Answer.objects.get(answer='answer1')
    self.assertEqual(str(answer), answer.answer)


