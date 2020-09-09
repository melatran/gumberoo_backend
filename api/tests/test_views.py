from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.models import Teacher
from api.models import Student

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

    self.assertEqual(response.status_code, 201)
    self.assertEqual(Student.objects.count(), 2)
    self.assertEqual(response.data['first_name'], data['first_name'])
