from django.test import TestCase
from api.popos import LessonScore, StudentScore

class PopoTest(TestCase):
  def setUp(self):
    self.student_score = StudentScore(student_id=1, average_score=80)
    self.lesson_score = LessonScore(lesson_id=1, average_score=73)

  def test_it_exists(self):
    self.assertIsInstance(self.student_score, StudentScore)
    self.assertIsInstance(self.lesson_score, LessonScore)

  def test_attributes(self):
    self.assertEqual(self.student_score.student_id, 1)
    self.assertEqual(self.student_score.average_score, 80)

    self.assertEqual(self.lesson_score.lesson_id, 1)
    self.assertEqual(self.lesson_score.average_score, 73)
