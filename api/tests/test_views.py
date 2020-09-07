from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import TeacherFactory, StudentFactory

class TeacherViewSet(TestCase):
  def setUp(self):
    self.teacher1 = TeacherFactory(first_name='teacher1First')
    self.teacher2 = TeacherFactory(first_name='teacher2First')
    self.teacher3 = TeacherFactory(first_name='teacher3First')

  def test_get_list(self):
    response = self.client.get('/teachers/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 3)
    self.assertEqual(response.data[0]['first_name'], self.teacher1.first_name)
  
  def test_get_detail(self):
    response = self.client.get('/teachers/%s/' % self.teacher1.id)

    import code; code.interact(local=dict(globals(), **locals()))

    self.assertEqual(response.status_code, 200)
