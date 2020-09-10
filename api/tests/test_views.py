import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.models import Teacher, Question, Student, Lesson, LessonStudent
from .factories import TeacherFactory, StudentFactory

class TeacherViewSet(TestCase):
  def setUp(self):
    self.teacher1 = TeacherFactory(first_name='teacher1First')
    self.teacher2 = TeacherFactory(first_name='teacher2First')
    self.teacher3 = TeacherFactory(first_name='teacher3First')
    

  def test_get_list(self):
    response = self.client.get('/api/v1/teachers/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 3)
    self.assertEqual(response.data[0]['id'], self.teacher1.id)
    self.assertEqual(response.data[0]['first_name'], self.teacher1.first_name)
  
  def test_get_detail(self):
    response = self.client.get('/api/v1/teachers/%s/' % self.teacher1.id)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['id'], self.teacher1.id)
    self.assertEqual(response.data['first_name'], self.teacher1.first_name)

  def test_post(self):
    data = {
      'first_name': 'newTeacher1First',
      'last_name': 'newTeacher1Last'
    }
    response = self.client.post('/api/v1/teachers/', data=data)

    self.assertEqual(response.status_code, 201)
    self.assertEqual(Teacher.objects.count(), 4)
    self.assertEqual(response.data['first_name'], data['first_name'])

  def test_teacher_student_get(self):
    Student.objects.create(first_name='max', last_name='ericson', age=5, teacher_id=self.teacher1.id)
    Student.objects.create(first_name='max2', last_name='ericson', age=5, teacher_id=self.teacher1.id)
    Student.objects.create(first_name='max3', last_name='ericson', age=5, teacher_id=self.teacher1.id)
    response = self.client.get('/api/v1/teachers/%s/students' % self.teacher1.id)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 3)

  def test_teacher_student_post(self): 
    data = {
      'id': 1,
      'students': [
        {
        'first_name': 'newStudent1First',
        'last_name': 'newStudent1Last',
        'age': 9
        },
        {
        'first_name': 'newStudent2First',
        'last_name': 'newStudent2Last',
        'age': 10
        }
      ]
    }
    response = self.client.post('/api/v1/teachers/%s/students' % self.teacher1.id, content_type='application/json', data=data)
   

    self.assertEqual(response.status_code, 200)
    self.assertEqual(Student.objects.count(), 2)
    self.assertEqual(response.data[0]['first_name'], data['students'][0]['first_name'])
    
class TeacherLessonSet(TestCase):
  def setUp(self):
    self.teacher1 = TeacherFactory(first_name='teacher1First', last_name='teacher1Last')

    self.lesson1 = self.teacher1.lesson_set.create(name='name1', description='description1')

    self.question1 = self.lesson1.question_set.create(question='question1', reading='reading1')
    self.answer1 = self.question1.answer_set.create(answer='answer1', correct=False)
    self.answer2 = self.question1.answer_set.create(answer='answer2', correct=True)

    self.question2 = self.lesson1.question_set.create(question='question2', reading='reading2')
    self.answer3 = self.question2.answer_set.create(answer='answer3', correct=True)
    self.answer4 = self.question2.answer_set.create(answer='answer4', correct=False)


  def test_can_post_lesson(self):
    data = {
      'lesson': {
        'name': 'lessonName1',
        'questions': [
            {
              'question': 'question1 description',
              'reading': 'question1 reading',
              'answers': [
                  {
                    'answer': 'answer1 description',
                    'correct': False
                  },
                  {
                    'answer': 'answer2 description',
                    'correct': False
                  },
                  {
                    'answer': 'answer3 description',
                    'correct': True
                  },
                  {
                    'answer': 'answer4 description',
                    'correct': False
                  }
                ]
            },
            {
              'question': 'question2 description',
              'reading': 'question2 reading',
              'answers': [
                  {
                    'answer': 'answer1 description',
                    'correct': False
                  },
                  {
                    'answer': 'answer2 description',
                    'correct': True
                  },
                  {
                    'answer': 'answer3 description',
                    'correct': False
                  },
                  {
                    'answer': 'answer4 description',
                    'correct': False
                  }
                ]
              }   
          ]
     }
 }

    response = self.client.post('/api/v1/teachers/%s/lessons/' % self.teacher1.id, data=data, content_type='application/json')

    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.data['name'], data['lesson']['name'])
    self.assertIsInstance(response.data['questions'][0], dict)
    self.assertIsInstance(response.data['questions'][1], dict)
    self.assertIsInstance(response.data['questions'][0]['answers'][0], dict)
    self.assertIsInstance(response.data['questions'][1]['answers'][0], dict)

  def test_can_get_lesson(self):
    response = self.client.get('/api/v1/lessons/%s/' % self.lesson1.id)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['name'], self.lesson1.name)
    self.assertIsInstance(response.data['questions'][0], dict)
    self.assertIsInstance(response.data['questions'][1], dict)
    self.assertIsInstance(response.data['questions'][0]['answers'][0], dict)
    self.assertIsInstance(response.data['questions'][1]['answers'][0], dict)


class StudentLessonViewSet(TestCase):
  def setUp(self):
    self.teacher = Teacher.objects.create(first_name='Severus', last_name='Snape')
    self.student = Student.objects.create(first_name='Draco', last_name='Malfoy', age= 13, teacher_id=self.teacher.id)
    self.lesson = self.teacher.lesson_set.create(name='Potions', description='Brew potions properly')

  def test_post_student_lesson(self):
    data = {
      "lesson": self.lesson.id,
      "score": 3,
      "mood": "I had a brilliant time"
    }
    response = self.client.post('/api/v1/students/%s' % (self.student.id), data=data, content_type='application/json')
   
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['score'], 3)
    self.assertEqual(response.data['mood'], 'I had a brilliant time')
    self.assertEqual(response.data['lesson'], 4)
    self.assertEqual(response.data['student'], 3)
