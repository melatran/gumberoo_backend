from django.test import TestCase
from api.models import Teacher, Student, Lesson

class TeacherModelTest(TestCase):
  def setUp(self):
    teacher = Teacher.objects.create(first_name='teacher1First', last_name='teacher1Last')
    teacher.student_set.create(first_name='student1First', last_name='student2Last', age=5)

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

