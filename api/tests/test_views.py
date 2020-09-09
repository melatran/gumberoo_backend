from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.models import Teacher

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

class TeacherLessonSet(TestCase):
  def setUp(self):
    self.teacher1 = TeacherFactory(first_name='teacher1First')

  def test_can_post_lesson(self):
    data = {
      'lesson': {
        'name': 'lessonName1',
        'questions': [
            {
              'desc': 'question1 description',
              'reading': 'question1 reading',
              'answers': [
                  {
                    'desc': 'answer1 description',
                    'correct': False
                  },
                  {
                    'desc': 'answer2 description',
                    'correct': False
                  },
                  {
                    'desc': 'answer3 description',
                    'correct': True
                  },
                  {
                    'desc': 'answer4 description',
                    'correct': False
                  }
                ]
            },
            {
              'desc': 'question2 description',
              'reading': 'question2 reading',
              'answers': [
                  {
                    'desc': 'answer1 description',
                    'correct': False
                  },
                  {
                    'desc': 'answer2 description',
                    'correct': True
                  },
                  {
                    'desc': 'answer3 description',
                    'correct': False
                  },
                  {
                    'desc': 'answer4 description',
                    'correct': False
                  }
                ]
              }   
          ]
     }
 }

    response = self.client.post('/api/v1/teachers/%s/lessons/' % self.teacher1.id, data=data, content_type='application/json')
    self.assertEqual(response.status_code, 201)
